import pygame.font

from color import Color
from settings import Setting


class Button(object):
    def __init__(self, screen, information, now_pos=None):
        """
        初始化按钮的属性
        :param settings:
        :param screen:
        :param information:文字信息
        :param now_pos:位置
        """
        # self.settings = settings
        self.settings = Setting()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = Color.blue.value
        self.text_color = Color.red.value

        # 使用什么字体来渲染文本,实参None使用默认字体，而48指定了文本的字号
        self.font = pygame.font.Font(self.settings.FONT, 35)

        # 创建按钮的rect对象，并使其居中
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)

        # 改变y轴坐标
        if now_pos is None:
            # 设为屏幕中间
            self.button_rect.center = self.screen_rect.center
        else:
            # 改变行
            self.button_rect.center = (
                self.screen_rect.centerx,
                self.screen_rect.centery * now_pos,
            )

        # 按钮的标签只需创建一次
        # 调用prep_msg()来处理这样的渲染,Pygame通过将你要显示的字符串渲染为图像来处理文本
        self.prep_msg(information)

    def prep_msg(self, information):
        """
        将msg渲染为图像，并使其在按钮上居中
        :param information:
        :return:
        """
        self.msg_image = self.font.render(
            information, True, self.text_color, self.button_color
        )
        """
        布尔实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）.余下的两个实参分别是文本颜色和背景色.
        我们启用了反锯齿功能，将文本的背景色设置为按钮的颜色（如果没有指定背景色，Pygame将以透明背景的方式渲染文本）
        """

        # 设置透明度
        # self.msg_image.set_alpha(100)

        # 调用font.render()将存储在msg中的文本转换为图像
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.button_rect.center

    def draw_button(self):
        """
        文本图像在按钮上居中：根据文本图像创建一个rect，并将其center属性设置为按钮的center属性
        :return:
        """
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_rect)
        # self.screen.set_alpha(50)
