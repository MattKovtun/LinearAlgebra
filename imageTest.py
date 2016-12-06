# from scipy import misc
# f = misc.face()
# misc.imsave('face.png', f)
# print("Resolution of the picture, and number of colors used in picture : " + str(f.shape))
# print("Color of 1st pixel in rgb:" + str(f[0][0]))
# print("Color of 2nd pixel in rgb:" + str(f[0][1]))
# print("Color of 3d pixel in rgb:" + str(f[0][2]))
# print(f)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage.interpolation




#
# img_data = mpimg.imread('face.png')
#
# new_data = scipy.ndimage.interpolation.rotate(img_data, 15)
# print(img_data)
# plt.imshow(new_data)  #this will show picture formed as array
# #plt.show()
# plt.savefig("/home/matt/PycharmProjects/LinearAlgebra/static/uploads/check.png")
#
# #mpimg.imsave("/home/matt/PycharmProjects/LinearAlgebra/static/uploads/check.png", img_data)





def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




def rotate_and_save(path, file_name):
    img_data = mpimg.imread(path + file_name)
    new_data = scipy.ndimage.interpolation.rotate(img_data, 75)
    plt.imshow(new_data)
    plt.savefig("/home/matt/PycharmProjects/LinearAlgebra/static/uploads/r" + file_name)