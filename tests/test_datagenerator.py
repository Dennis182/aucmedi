#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2020 IT-Infrastructure for Translational Medical Research,    #
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
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
#External libraries
import unittest
import numpy as np
import tempfile
from PIL import Image
import os
#Internal libraries
from aucmedi import DataGenerator

#-----------------------------------------------------#
#             Unittest: Data Augmentation             #
#-----------------------------------------------------#
class DataGeneratorTEST(unittest.TestCase):
    # Create random imaging and segmentation data
    @classmethod
    def setUpClass(self):
        np.random.seed(1234)
        # Initialize temporary directory
        self.tmp_data = tempfile.TemporaryDirectory(prefix="tmp.aucmedi.",
                                                    suffix=".data")
        # Create Grayscale data
        self.sampleList_gray = []
        for i in range(0, 25):
            img_gray = np.random.rand(16, 16) * 255
            imgGRAY_pillow = Image.fromarray(img_gray.astype(np.uint8))
            index = "image.sample_" + str(i) + ".GRAY.png"
            path_sampleGRAY = os.path.join(self.tmp_data.name, index)
            imgGRAY_pillow.save(path_sampleGRAY)
            self.sampleList_gray.append(index)

        # Create RGB data
        img_rgb = np.random.rand(16, 16, 3) * 254
        self.imgRGB = np.float32(img_rgb)

        # Create RGB data
        self.sampleList_rgb = []
        for i in range(0, 25):
            img_rgb = np.random.rand(16, 16, 3) * 255
            imgRGB_pillow = Image.fromarray(img_rgb.astype(np.uint8))
            index = "image.sample_" + str(i) + ".RGB.png"
            path_sampleRGB = os.path.join(self.tmp_data.name, index)
            imgRGB_pillow.save(path_sampleRGB)
            self.sampleList_rgb.append(index)

    #-------------------------------------------------#
    #                Base Functionality               #
    #-------------------------------------------------#
    # Class Creation
    def test_DATAGENERATOR_BASE_create(self):
        data_gen = DataGenerator(self.sampleList_rgb, self.tmp_data.name)
        self.assertIsInstance(data_gen, DataGenerator)

    # Usage: Grayscale without Labels
    def test_DATAGENERATOR_BASE_run_GRAYSCALE_noLabel(self):
        data_gen = DataGenerator(self.sampleList_gray, self.tmp_data.name,
                                 grayscale=True, batch_size=5)
        for i in range(0, 10):
            batch = next(data_gen)
            self.assertTrue(len(batch), 1)
            self.assertTrue(np.array_equal(batch[0].shape, (5, 224, 224, 1)))

    # Usage: RGB without Labels
    def test_DATAGENERATOR_BASE_run_RGB_noLabel(self):
        data_gen = DataGenerator(self.sampleList_rgb, self.tmp_data.name,
                                 grayscale=False, batch_size=5)
        for i in range(0, 10):
            batch = next(data_gen)
            self.assertTrue(len(batch), 1)
            self.assertTrue(np.array_equal(batch[0].shape, (5, 224, 224, 3)))