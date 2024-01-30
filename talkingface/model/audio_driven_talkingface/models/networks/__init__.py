# Copyright (c) 2019, NVIDIA Corporation. All rights reserved.
#
# This work is made available
# under the Nvidia Source Code License (1-way Commercial).
# To view a copy of this license, visit
# https://nvlabs.github.io/few-shot-vid2vid/License.txt
import torch
import torch.nn as nn
import functools
import numpy as np
import torch.nn.functional as F
from models.networks.loss import *
from models.networks.discriminator import *
from models.networks.normalization import get_nonspade_norm_layer
from models.modules.linear_combine import LinearCombineModule
from models.modules.spade_combine import SpadeCombineModule

import pdb

def modify_commandline_options(parser, is_train):
    opt, _ = parser.parse_known_args()
    if 'fewshot' in opt.netG:
        parser = FewShotGenerator.modify_commandline_options(parser, is_train)
    
    if is_train:
        if opt.which_model_netD == 'multiscale':
            parser = MultiscaleDiscriminator.modify_commandline_options(parser, is_train)
        elif opt.which_model_netD == 'n_layers':
            parser = NLayerDiscriminator.modify_commandline_options(parser, is_train)
        elif opt.which_model_netD == 'syncframe':
            parser = SepDiscriminator.modify_commandline_options(parser, is_train)
    return parser
    
def define_G(opt):    
    if 'fewshot' in opt.netG:
        # netG = FewShotGenerator(opt)
        if opt.spade_combine:
            netG = SpadeCombineModule(opt)
        else:
            netG = LinearCombineModule(opt)
    else:
        raise('generator not implemented!')
    if opt.isTrain and opt.print_G: netG.print_network()
    if len(opt.gpu_ids) > 0:
        assert(torch.cuda.is_available())   
        netG.cuda()
    netG.init_weights(opt.init_type, opt.init_variance)
    return netG

def define_D(opt, input_nc, ndf, n_layers_D, norm='spectralinstance', subarch='n_layers', num_D=1, getIntermFeat=False, stride=2, gpu_ids=[]):
    norm_layer = get_nonspade_norm_layer(opt, norm_type=norm)
    if opt.which_model_netD == 'multiscale':
        netD = MultiscaleDiscriminator(opt, input_nc, ndf, n_layers_D, norm_layer, subarch, num_D, getIntermFeat, stride, gpu_ids)
    elif opt.which_model_netD == 'n_layers':
        netD = NLayerDiscriminator(input_nc, ndf, n_layers_D, norm_layer, getIntermFeat)
    elif opt.which_model_netD == 'syncframe':
        if subarch == 'sync':
            netD = SyncDiscriminator(opt, 64, ndf, 256, 2, 5)
        elif subarch == 'frame':
            netD = FrameDiscriminator(opt, 256, input_nc, ndf, 6)
        elif subarch == 'syncframe':
            netD = SepDiscriminator(opt, ndf, 256, 1920)
    elif opt.which_model_netD == 'sepfea':
        if subarch == 'mouth':
            netD = AudioFeaDiscriminator(input_nc, ndf, n_layers_D, norm_layer, getIntermFeat, stride, nf_final=256)
        else:
            netD = SepFeaDiscriminator(opt, ndf, n_layers_D, norm_layer, getIntermFeat, stride)
    else:
        raise('unknown type discriminator %s!' % opt.which_model_netD)
        
    if opt.isTrain and opt.print_D: netD.print_network()
    if len(gpu_ids) > 0:
        assert(torch.cuda.is_available())
        netD.cuda()
    netD.init_weights(opt.init_type, opt.init_variance)
    return netD
