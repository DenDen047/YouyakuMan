import os
import torch
from torch import nn
from pytorch_pretrained_bert import BertModel
import pdb

from models.encoder import TransformerInterEncoder
from LangFactory import LangFactory


class Bert(nn.Module):
    def __init__(self, bert_model, temp_dir):
        super(Bert, self).__init__()
        self.model = BertModel.from_pretrained(bert_model, cache_dir=temp_dir)

    def forward(self, x, segs, mask):
        encoded_layers, _ = self.model(x, segs)
        # encoded_layers, _ = self.model(x, segs, attention_mask=mask)
        top_vec = encoded_layers[-1]
        return top_vec


class Summarizer(nn.Module):
    def __init__(self, opt, lang):
        super(Summarizer, self).__init__()
        self.langfac = LangFactory(lang)
        if lang == 'jp':
            dirname = 'Japanese'
        elif lang == 'en':
            dirname = 'English'
        else:
            dirname = 'Others'
        temp_dir = os.path.join('/model', dirname)
        self.bert = Bert(self.langfac.toolkit.bert_model, temp_dir=temp_dir)
        self.encoder = TransformerInterEncoder(self.bert.model.config.hidden_size,
                                               opt['ff_size'],
                                               opt['heads'],
                                               opt['dropout'],
                                               opt['inter_layers'])

    def load_cp(self, pt):
        self.load_state_dict(pt, strict=True)

    def forward(self, x, segs, clss, mask, mask_cls, sentence_range=None):
        top_vec = self.bert(x, segs, mask)
        sents_vec = top_vec[torch.arange(top_vec.size(0)).unsqueeze(1), clss]
        print(sents_vec.shape)
        print(mask_cls[:, :, None].shape)
        sents_vec = sents_vec * mask_cls[:, :, None].float()
        sent_scores = self.encoder(sents_vec, mask_cls).squeeze(-1)
        return sent_scores, mask_cls


class ModelLoader(Summarizer):
    def __init__(self, cp, opt, lang):
        cp_statedict = torch.load(cp, map_location=lambda storage, loc: storage)
        opt = dict(torch.load(opt))
        super(ModelLoader, self).__init__(opt, lang)
        self.load_cp(cp_statedict)
        self.eval()
