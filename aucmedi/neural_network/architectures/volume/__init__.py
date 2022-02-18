#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
# Abstract Base Class for Architectures
from aucmedi.neural_network.architectures.arch_base import Architecture_Base

#-----------------------------------------------------#
#                    Architectures                    #
#-----------------------------------------------------#
# Vanilla Classifier
from aucmedi.neural_network.architectures.volume.vanilla import Architecture_Vanilla
# DenseNet
from aucmedi.neural_network.architectures.volume.densenet121 import Architecture_DenseNet121
from aucmedi.neural_network.architectures.volume.densenet169 import Architecture_DenseNet169
from aucmedi.neural_network.architectures.volume.densenet201 import Architecture_DenseNet201
# EfficientNet
from aucmedi.neural_network.architectures.volume.efficientnetb0 import Architecture_EfficientNetB0
# from aucmedi.neural_network.architectures.volume.efficientnetb1 import Architecture_EfficientNetB1
# from aucmedi.neural_network.architectures.volume.efficientnetb2 import Architecture_EfficientNetB2
# from aucmedi.neural_network.architectures.volume.efficientnetb3 import Architecture_EfficientNetB3
# from aucmedi.neural_network.architectures.volume.efficientnetb4 import Architecture_EfficientNetB4
# from aucmedi.neural_network.architectures.volume.efficientnetb5 import Architecture_EfficientNetB5
# from aucmedi.neural_network.architectures.volume.efficientnetb6 import Architecture_EfficientNetB6
# from aucmedi.neural_network.architectures.volume.efficientnetb7 import Architecture_EfficientNetB7

#-----------------------------------------------------#
#       Access Functions to Architecture Classes      #
#-----------------------------------------------------#
# Architecture Dictionary
architecture_dict = {
    "Vanilla": Architecture_Vanilla,
    "DenseNet121": Architecture_DenseNet121,
    "DenseNet169": Architecture_DenseNet169,
    "DenseNet201": Architecture_DenseNet201,
    "EfficientNetB0": Architecture_EfficientNetB0,
    # "EfficientNetB1": Architecture_EfficientNetB1,
    # "EfficientNetB2": Architecture_EfficientNetB2,
    # "EfficientNetB3": Architecture_EfficientNetB3,
    # "EfficientNetB4": Architecture_EfficientNetB4,
    # "EfficientNetB5": Architecture_EfficientNetB5,
    # "EfficientNetB6": Architecture_EfficientNetB6,
    # "EfficientNetB7": Architecture_EfficientNetB7,
}
# List of implemented architectures
architectures = list(architecture_dict.keys())

#-----------------------------------------------------#
#       Meta Information of Architecture Classes      #
#-----------------------------------------------------#
# Utilized standardize mode of architectures required for Transfer Learning
supported_standardize_mode = {
    "Vanilla": "z-score",
    "DenseNet121": "torch",
    "DenseNet169": "torch",
    "DenseNet201": "torch",
    "EfficientNetB0": "caffe",
    "EfficientNetB1": "caffe",
    "EfficientNetB2": "caffe",
    "EfficientNetB3": "caffe",
    "EfficientNetB4": "caffe",
    "EfficientNetB5": "caffe",
    "EfficientNetB6": "caffe",
    "EfficientNetB7": "caffe",
}