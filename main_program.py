
import os
import sys
import subprocess
from PyQt4 import QtGui, QtCore

paths = '/home/samy/Bureau/script/script python/usingQT/ui', '/home/samy/Bureau/script/script python/usingQT'

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

from Image_operation import image_operation
from main_window import main_window as MW


# Application that use QT
app_1 = QtGui.QApplication(sys.argv)

#instantiate class image operation
img_op = image_operation()

# Instantiate main window here
window_primary = MW(menu_bar=1)
def undo_action():
    img_op.current_image_entity = img_op.old_entity
    try:
        pixmap= pil2qpixmap(img_op.ubuntu_fix_qt(img_op.current_image_entity))
        window_primary.show_image(pixmap)
    except Exception, err:
        print err

def save_image():
    """
    save image via qt dialog box
    return str path 
    """
    img_path = str(QtGui.QFileDialog.getSaveFileName(filter='*.png'))
    print "save at %s" % img_path

    pixmap= pil2qpixmap(img_op.ubuntu_fix_qt(img_op.current_image_entity))
    pixmap.save(img_path, "PNG")
    return img_path

def load_image():

    img_path = str(QtGui.QFileDialog.getOpenFileName())
    img_op.load_image(img_path)
    window_primary.load_image(img_path)

def pil2qpixmap(pil_image):
    
    qimage = QtGui.QImage(pil_image).convertToFormat(QtGui.QImage.Format_ARGB32)
    
    pix = QtGui.QPixmap.fromImage(qimage)
    
    print "pix done"
    return pix

def launch_blender():
    """
    just launching blender with no arguments
    """
    print "Launch blender"
    processes.add(subprocess.Popen([os.system('/home/samy/Bureau/blender-2.72-linux-glibc211-i686/blender'), 'blender']))


def launch_stream_cam_ubuntu():
    """
    just launch cheese (ubuntu webcam manager) without arguments
    """
    print "launch webcam"
    processes.add(subprocess.Popen([os.system('cheese'),'cheese']))

def launch_contrast_action():
    """
    Use image_operation and main_window class to control contrast of image
    """
    def change_image():
        value = int(slider.value())
        image =img_op.contrast_image(value/10)
        window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))
        print 'value slider : ', value

    window_contrast = MW(menu_bar=0)
    label_contrast = QtGui.QLabel(window_contrast)
    label_contrast.setText("Contrast Value :")
    window_contrast.setWindowTitle('contrast')
    
    window_contrast.mainLayout.addWidget(label_contrast)

    slider = QtGui.QSlider(window_contrast)
    slider.setOrientation(QtCore.Qt.Horizontal)
    slider.valueChanged.connect(change_image)
    window_contrast.mainLayout.addWidget(slider)

    
    window_contrast.show()

    #image =img_op.contrast_image(0)
    
    print "done contrast image"
    
    window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))

def launch_brightness_action():
    """
    Use image_operation and main_window class to control contrast of image
    """
    def change_image():
        value = int(slider.value())
        image =img_op.brightness_image(value/10)
        window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))
        print 'value slider : ', value

    window_brightness = MW(menu_bar=0)
    label_brightness = QtGui.QLabel(window_brightness)
    label_brightness.setText("Brightness Value :")
    window_brightness.setWindowTitle('brightness')
    
    window_brightness.mainLayout.addWidget(label_brightness)

    slider = QtGui.QSlider(window_brightness)
    slider.setOrientation(QtCore.Qt.Horizontal)
    slider.valueChanged.connect(change_image)
    window_brightness.mainLayout.addWidget(slider)
    
    window_brightness.show()

    #image =img_op.contrast_image(0)
    
    print "done contrast image"
    window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))


def launch_sharpen_action():
    """
    Use image_operation and main_window class to control contrast of image
    """
    def change_image():
        value = int(slider.value())
        image =img_op.sharpen_image(value/10)
        window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))
        print 'value slider : ', value

    window_sharpen = MW(menu_bar=0)
    label_sharpen = QtGui.QLabel(window_sharpen)
    label_sharpen.setText("sharpen Value :")
    window_sharpen.setWindowTitle('sharpen')
    
    window_sharpen.mainLayout.addWidget(label_sharpen)

    slider = QtGui.QSlider(window_sharpen)
    slider.setOrientation(QtCore.Qt.Horizontal)
    slider.valueChanged.connect(change_image)
    window_sharpen.mainLayout.addWidget(slider)
    
    window_sharpen.show()

    #image =img_op.contrast_image(0)
    
    print "done contrast image"
    window_primary.show_image(pil2qpixmap(img_op.ubuntu_fix_qt(image)))



processes = set()

file_open_Action = QtGui.QAction("&Open", window_primary)
file_open_Action.setShortcut("Ctrl+O")
file_open_Action.setStatusTip('Open File')
file_open_Action.triggered.connect(load_image)

window_primary.add_menu_elements(file_open_Action,'File')

file_save_Action = QtGui.QAction("&Save", window_primary)
file_save_Action.setShortcut("Ctrl+S")
file_save_Action.setStatusTip('Save File')
file_save_Action.triggered.connect(save_image)

window_primary.add_menu_elements(file_save_Action,'File')

# action process to derrive
Undo_action = QtGui.QAction("&UNDO", window_primary)
Undo_action.setStatusTip('undo to last operation')
Undo_action.triggered.connect(undo_action)
Undo_action.setShortcut("Ctrl+Z")
window_primary.add_menu_elements(Undo_action,'Action')

contrast_Action = QtGui.QAction("&Image contrast", window_primary)
contrast_Action.setStatusTip('adjust contrast')
contrast_Action.triggered.connect(launch_contrast_action)


window_primary.add_menu_elements(contrast_Action,'Action')


brightness_Action = QtGui.QAction("&Image brightness", window_primary)
brightness_Action.setStatusTip('adjust brightness')
brightness_Action.triggered.connect(launch_brightness_action)


window_primary.add_menu_elements(brightness_Action,'Action')


sharpen_Action = QtGui.QAction("&Image sharpen", window_primary)
sharpen_Action.setStatusTip('adjust sharpen')
sharpen_Action.triggered.connect(launch_sharpen_action)


window_primary.add_menu_elements(sharpen_Action,'Action')


blender_Action = QtGui.QAction("&Launch blender", window_primary)
blender_Action.setShortcut("Ctrl+B")
blender_Action.setStatusTip('Launching Blender')
blender_Action.triggered.connect(launch_blender)


window_primary.add_menu_elements(blender_Action,'Action')


cam_action = QtGui.QAction('&launch wbecam assist',window_primary)
cam_action.setShortcut("Ctrl+C")
cam_action.setStatusTip('Launching webcam')
cam_action.triggered.connect(launch_stream_cam_ubuntu)   


window_primary.add_menu_elements(cam_action,'Action')

window_primary.draw_window()

app_1.exec_()

