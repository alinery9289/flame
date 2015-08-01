import sys
import os
from subprocess import Popen, PIPE

def neural_talk(filename):
    """
    call neural talk API on the given image
    @filename - image file with absolute path
    @return description string about the image
    """
    image_dir, image_name = os.path.split(filename)
    print("image directory: %s" % image_dir)
    print("image to be processed: %s" % image_name)

    p = Popen(['sh',
        '/home/medialab/deploy/imageDsp/applications/neuraltalk-mix/pre_mix.sh',
        image_dir, image_name], stdout=PIPE)

    with p.stdout:
        for line in iter(p.stdout.readline, b''):
            if 'PRED:' in line:
                print("============ GOT RESULT ============")
                print("neural_talk_result: ", line)
                print("============ GOT RESULT ============")
                return line


if __name__ == '__main__':
    neural_talk("/home/medialab/deploy/imagecache/2.jpg")