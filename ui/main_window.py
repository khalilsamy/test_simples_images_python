import sys
from PyQt4 import QtGui, QtCore
import os
sys.path.append('/home/samy/Bureau/script/script python/shotgun/coding_yak')

from logger import logger

log = logger()

class main_window(QtGui.QMainWindow):
    """
    This class create ui window with PyQt4, class give main window which can be easly
    heritate

    public attributes : 
    qt_window
    qt_layout
    menu_bar
    palette

    """
    def __init__(self, menu_bar = False):
        
        # init of master class
        self.qt_window = super(main_window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        
        self.statusBar()

        self.mainLayout = QtGui.QVBoxLayout()

        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        
        self.setCentralWidget(self.centralWidget)
        self.label = QtGui.QLabel()
        if menu_bar:
            log.info('menu_bar valide')
            self.qt_menu_bar = self.menuBar()
            self.qt_menu_bar.setNativeMenuBar(False)
            self.list_menu_name = []
             
        self.palette = None

    def add_menu_elements(self, obj,menu_name):
        """
        function to add elements in main_window_layout menu
        """
        # we check if our menu option exist:
        if not menu_name  in self.list_menu_name:
            self.fileMenu_entity = self.qt_menu_bar.addMenu('&%s'% menu_name)
            self.list_menu_name.append(menu_name)
        self.fileMenu_entity.addAction(obj)
    
    def load_image(self,image_path):
        """
        using open dialog box qt lo open image
        return image_path
        """
        
        pixmap = QtGui.QPixmap(image_path)
        
        self.label.setPixmap(pixmap)
        self.mainLayout.addWidget(self.label)
        self.update()
    
    def show_image(self, pixmap):
        print "show_image "
        self.label.setPixmap(pixmap)
        self.mainLayout.addWidget(self.label)
        
        self.update()

    #--- QT OBJECTS ----#
    def draw_window(self):
        """
        this function draw window from pattern and return instance window
        """
        self.show()
    """
                def save_image(self,path,pix_img):
                    pixmap = QtGui.QPixmap()"""

#-------- MAIN --------#
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)

    window = main_window(menu_bar = True)
    window.draw_window()
    app.exec_()
    """
    button = QPushButton("launch blender", None)
    button.clicked.connect(launch_blender)
    button.show()
    app.exec_()"""