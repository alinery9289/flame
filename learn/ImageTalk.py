import sys
import os
import logging
from subprocess import Popen, PIPE

logger = logging.getLogger(__name__)

def neural_talk(image_dir, images):
    """
    call neural talk API on the given image

    @param image_dir - absolute path of image file folder (work dir)
    @param images - a list containing name of images to be processed
    @return description list
    """
    num_images = len(images)
    if num_images < 1:
        print("no input image found")
        return "ERROR: input image not found"

    print("image directory: %s" % image_dir)
    print("images to be processed: ", images)
    logger.info("processing images: %s" % images)

    cmd = ['sh',
            '/home/medialab/deploy/imageDsp/applications/neuraltalk-mix/pre_mix.sh',
            image_dir]
    cmd.extend(images)
    p = Popen(cmd, stdout=PIPE)

    with p.stdout:
        image_id = 1
        descriptions = []
        for line in iter(p.stdout.readline, b''):
            if 'PRED:' in line:
                dsp = "image[{0}]: {1}".format(image_id, line)
                print(dsp)
                image_id += 1
                descriptions.append(dsp)
        logger.info("neural talk job finish")
        return descriptions


if __name__ == '__main__':
    neural_talk("/home/medialab/deploy/imagecache/",
            ["1.jpg", "2.jpg", "3.jpg", "4.jpg"])
