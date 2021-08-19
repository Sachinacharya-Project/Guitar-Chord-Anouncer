from PyQt5 import QtCore, QtGui, QtWidgets
import os, time, random, pyttsx3

MEDIA_LOCATIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0])
engine.setProperty('volume', 1)

def speak(text):
        engine.say(text)
        engine.runAndWait()

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(825, 600)
                MainWindow.setMinimumSize(QtCore.QSize(800, 600))
                MainWindow.setMaximumSize(QtCore.QSize(825, 600))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/assets/icons/music player.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background: rgba(0, 0, 0, 0.1);\n"
        "border-radius: 10px;\n"
        "color: white;\n"
        "padding: 10px;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
                self.stackedWidget.setObjectName("stackedWidget")
                self.start_page = QtWidgets.QWidget()
                self.start_page.setObjectName("start_page")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.start_page)
                self.verticalLayout.setObjectName("verticalLayout")
                spacerItem = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout.addItem(spacerItem)
                self.label = QtWidgets.QLabel(self.start_page)
                font = QtGui.QFont()
                font.setFamily("Origin Tech Demo")
                font.setPointSize(32)
                self.label.setFont(font)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.verticalLayout.addWidget(self.label)
                spacerItem1 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout.addItem(spacerItem1)
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem2)
                self.start_btn = QtWidgets.QPushButton(self.start_page)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
                self.start_btn.setSizePolicy(sizePolicy)
                self.start_btn.setMinimumSize(QtCore.QSize(200, 49))
                self.start_btn.setMaximumSize(QtCore.QSize(200, 49))
                font = QtGui.QFont()
                font.setFamily("Starcraft")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.start_btn.setFont(font)
                self.start_btn.setStyleSheet("QPushButton{padding: 5px;\n"
        "border: 1px solid #333;\n"
        "background: #222;\n"
        "color: white;\n"
        "border-radius: 20px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "color: rgba(255, 255, 255, 0.8)\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background: #111;\n"
        "}")
                self.start_btn.setObjectName("start_btn")
                self.start_btn.clicked.connect(self.change_window)
                self.horizontalLayout.addWidget(self.start_btn)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem3)
                self.verticalLayout.addLayout(self.horizontalLayout)
                spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem4)
                self.stackedWidget.addWidget(self.start_page)
                self.second_page = QtWidgets.QWidget()
                self.second_page.setObjectName("second_page")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.second_page)
                self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.image_label = QtWidgets.QLabel(self.second_page)
                self.image_label.setText("")
                self.image_label.setPixmap(QtGui.QPixmap(""))
                self.image_label.setScaledContents(True)
                self.image_label.setObjectName("image_label")
                self.gridLayout_2.addWidget(self.image_label, 0, 0, 1, 1)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setSpacing(2)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.chord_name = QtWidgets.QLabel(self.second_page)
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.chord_name.setFont(font)
                self.chord_name.setAlignment(QtCore.Qt.AlignCenter)
                self.chord_name.setObjectName("chord_name")
                self.horizontalLayout_2.addWidget(self.chord_name)
                self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
                self.gridLayout_2.setRowStretch(0, 2)
                self.gridLayout_2.setRowStretch(1, 1)
                self.stackedWidget.addWidget(self.second_page)
                self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.thread = WorkingThread()
                self.thread.chordsinfo.connect(self.update_info)
        def update_info(self, data):
                self.change_image(data)
        def change_window(self):
                self.stackedWidget.setCurrentWidget(self.second_page)
                self.thread.start()
        def change_image(self, image_name):
                _translate = QtCore.QCoreApplication.translate
                image = os.path.join(MEDIA_LOCATIONS, "{}.jpg".format(image_name))
                self.image_label.setPixmap(QtGui.QPixmap(image))
                self.image_label.setScaledContents(True)
                self.chord_name.setText(_translate("MainWindow", "{} Chord".format(image_name)))
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Random Chords Chooser"))
                self.label.setText(_translate("MainWindow", "Welcome to\n"
        "Random Chords"))
                self.start_btn.setText(_translate("MainWindow", "Start"))
                self.chord_name.setText(_translate("MainWindow", "A Major Chord"))
class WorkingThread(QtCore.QThread):
        chordsinfo = QtCore.pyqtSignal(str)
        def run(self):
                chords_list = [
                        '"A" Major',
                        '"A" Minor',
                        "C Major",
                        "D Major",
                        "E Major",
                        "E Minor",
                        "G Major"
                ]
                time_list = [2, 4, 5, 6, 10]
                while True:
                        selected_chord = chords_list[random.randint(0, len(chords_list) - 1)]
                        print(selected_chord)
                        selected_time = time_list[random.randint(0, len(time_list) - 1)]
                        selected_chord_ = selected_chord.replace('"', '')
                        self.chordsinfo.emit(selected_chord_)
                        speak(selected_chord)
                        time.sleep(int(selected_time))
import resources_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
