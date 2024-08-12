from live2d_widget_python import Live2DWidget
# 如果你使用的是PyQt5，可以将Live2DWidget嵌入到应用中
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# 创建一个Live2DWidget实例
widget = Live2DWidget()

# 加载一个Live2D模型
widget.loadModel('model.model.json')  # 请确保model.model.json文件在可访问的路径

# 设置模型的位置
widget.setModelPosition(100, 200)

# 开始更新模型
widget.start()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Live2D Model Example')
        self.setGeometry(100, 100, 800, 600)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        layout = QVBoxLayout()
        layout.addWidget(widget)  # 将Live2DWidget添加到布局中
        self.widget.setLayout(layout)


# 创建应用并显示主窗口
app = QApplication([])
window = MainWindow()
window.show()

# 开始应用的事件循环
app.exec_()
