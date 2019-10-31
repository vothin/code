#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: cloudDPageView.py
    @time: 2019/10/12 10:11
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class CloudDPage(BusinessView):
    # 我的
    mine_view = (By.ID, 'com.wdkl.capacity_care_user:id/rl_mine_right')
    mineName_text = (By.ID, 'com.wdkl.capacity_care_user:id/user_name')
    mineImage_button = (By.ID, 'com.wdkl.capacity_care_user:id/image')

    # 标题页
    cloudDPageAll_button = (By.ID, 'com.wdkl.capacity_care_user:id/main_all_btn')
    cloudDPageGuanzhu_button = (By.ID, 'com.wdkl.capacity_care_user:id/main_guanzhu_btn')
    cloudDPagePindao_button = (By.ID, 'com.wdkl.capacity_care_user:id/main_pindao_btn')
    cloudDPageTuijian_button = (By.ID, 'com.wdkl.capacity_care_user:id/main_tuijian_btn')

    # 帖子相关
    # 用户
    blogPostName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_name')
    blogPostTime_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_time')
    blogPostGuanzhu_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_gz')
    blogPostContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_content')
    blogPostContent2_text = (By.ID, 'com.wdkl.capacity_care_user:id/ll01')


    # 点赞
    blogPostLike_button = (By.ID, 'com.wdkl.capacity_care_user:id/iv_like')
    blogPostLikeCount_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_like_cont')
    blogPostLikeName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_digg_name')

    # 回复
    blogPostReply_button = (By.ID, 'com.wdkl.capacity_care_user:id/iv_reply')
    blogPostReplyCount_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_reply_count')
    blogPostReplyName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_reply_name')
    blogPostReplyContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_command_content')
    blogPostReplyComment_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_comment')
    blogPostReplySendComment_button = (By.ID, 'com.wdkl.capacity_care_user:id/btn_send_comment')

    blogPostReplyBut_button = (By.ID, 'com.wdkl.capacity_care_user:id/menu_button')


    # 更多
    blogPostMore_button = (By.ID, 'com.wdkl.capacity_care_user:id/iv_more')
    blogPostMoreCollect_button = (By.ID, 'com.wdkl.capacity_care_user:id/iv_collect')
    blogPostMoreCancel_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_cancel')

    # 帖子详情界面
    blogPostDetailsLike_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_digg')
    blogPostDetailsLikeName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_name')

    blogPostDetailsReplyName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_name')
    blogPostDetailsReplyContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_command_content')

    blogPostDetailsReplyBut_button = (By.ID, 'com.wdkl.capacity_care_user:id/menu_button')


    # sns返回
    blogPostBack_button = (By.ID, 'com.wdkl.capacity_care_user:id/titlebar_left')


    # 用户
    mineName = ''
    blogPostName = ''
    blogPostGuanzhuOld = ''
    blogPostGuanzhuNew = ''

    # 点赞
    blogPostLikeNameList = []
    blogPostLikeName = ''
    blogPostDetailsLikeName = ''
    blogPostLikeCountOld = ''
    blogPostLikeCountNew = ''

    # 回复
    blogPostReplyName = ''
    blogPostDetailsReplyName = ''
    blogPostReplyCountOld = ''
    blogPostReplyCountNew = ''
    blogPostReplyComment = ''
    blogPostReplyContent = ''
    blogPostDetailsReplyContent = ''
    blogPostDetailsReplyCountOld = ''
    blogPostDetailsReplyCountNew = ''

    # 收藏
    blogPostContentOld = ''
    blogPostContentNew = ''



    # 关注用户
    def blogPostAttention(self):
        self.cloudDEachPageView(0)
        logging.info('=============点击全部界面=============')
        self.find_element(*self.cloudDPageAll_button).click()

        self.blogPostGuanzhuOld = self.find_elements(*self.blogPostGuanzhu_text)[0].text

        if self.blogPostGuanzhuOld == '+关注':
            logging.info('=============点击关注用户=============')
            self.find_elements(*self.blogPostGuanzhu_text)[0].click()

            self.blogPostGuanzhuNew = self.find_elements(*self.blogPostGuanzhu_text)[0].text
            return self.blogPostGuanzhuNew

        elif self.blogPostGuanzhuOld == '取消关注':
            logging.info('=============取消关注用户=============')
            self.find_elements(*self.blogPostGuanzhu_text)[0].click()

            self.blogPostGuanzhuNew = self.find_elements(*self.blogPostGuanzhu_text)[0].text
            return self.blogPostGuanzhuNew

    # 检查关注用户
    def check_blogPostAttention(self):
        if self.blogPostGuanzhuOld == '+关注' \
            and self.blogPostGuanzhuNew == '取消关注':
            logging.info('=============关注成功=============')
            return True

        elif self.blogPostGuanzhuOld == '取消关注' \
            and self.blogPostGuanzhuNew == '+关注':
            logging.info('=============取消关注成功=============')
            return True

        else:
            logging.info('=============关注失败=============')
            self.getScreenShot('云医圈界面-关注')
            return False



    # 点赞
    def blogPostLike(self):
        self.cloudDEachPageView(0)
        logging.info('=============点击全部界面=============')
        self.find_element(*self.cloudDPageAll_button).click()

        time.sleep(3)
        logging.info('=============点击帖子=============')
        self.find_elements(*self.blogPostContent2_text)[0].click()

        time.sleep(3)
        try:
            self.find_element(*self.blogPostDetailsLike_button)
        except:
            logging.info('=============没人点赞=============')
            self.find_element(*self.blogPostBack_button).click()
            self.blogPostLikeCountOld = self.find_elements(*self.blogPostLikeCount_text)[0].text
        else:
            logging.info('=============获得点赞人员列表=============')
            self.find_element(*self.blogPostDetailsLike_button).click()

            time.sleep(3)
            a = self.find_elements(*self.blogPostDetailsLikeName_text)
            for i in range(len(a)):
                self.blogPostLikeNameList.append(self.find_elements(*self.blogPostDetailsLikeName_text)[i].text)
            logging.info('=============点赞人员列表：%s=============' % self.blogPostLikeNameList)

            time.sleep(3)
            if self.mineName not in self.blogPostLikeNameList:
                logging.info('=============用户不在点赞人员列表=============')
                self.find_element(*self.blogPostBack_button).click()
                self.find_element(*self.blogPostBack_button).click()
                self.blogPostLikeCountOld = self.find_elements(*self.blogPostLikeCount_text)[0].text


            else:
                logging.info('=============用户在点赞人员列表=============')
                self.find_element(*self.blogPostBack_button).click()
                self.find_element(*self.blogPostBack_button).click()
                self.find_elements(*self.blogPostLike_button)[0].click()
                self.blogPostLikeCountOld = self.find_elements(*self.blogPostLikeCount_text)[0].text

        finally:
            time.sleep(3)
            logging.info('=============点赞=============')
            self.find_elements(*self.blogPostLike_button)[0].click()

            x1 = 0.5
            y1 = 0.2
            y2 = 0.8
            self.swipe(x1, y1, x1, y2, 1000)
            time.sleep(3)
            self.blogPostLikeName = (self.find_elements(*self.blogPostLikeName_text)[0].text)[:-1]
            self.blogPostLikeCountNew = self.find_elements(*self.blogPostLikeCount_text)[0].text

            time.sleep(3)
            logging.info('=============查看点赞人列表=============')
            self.find_elements(*self.blogPostContent2_text)[0].click()
            self.find_element(*self.blogPostDetailsLike_button).click()

            time.sleep(5)
            try:
                self.find_elements(*self.blogPostDetailsLikeName_text)
            except:
                self.getScreenShot('点赞人列表')
            else:
                self.blogPostDetailsLikeName = self.find_elements(*self.blogPostDetailsLikeName_text)[0].text

            self.find_element(*self.blogPostBack_button).click()
            time.sleep(3)
            self.find_element(*self.blogPostBack_button).click()


    def check_blogPostLike(self):
        time.sleep(3)
        self.cloudDEachPageView(0)
        logging.info('=============我的界面用户名：%s=============' % self.mineName)
        logging.info('=============点赞界面用户名：%s=============' % self.blogPostLikeName)
        logging.info('=============点赞列表用户名：%s=============' % self.blogPostDetailsLikeName)

        logging.info('=============旧的点赞数量：%s=============' % self.blogPostLikeCountOld)
        logging.info('=============新的点赞数量：%s=============' % self.blogPostLikeCountNew)

        if self.mineName == self.blogPostLikeName == self.blogPostDetailsLikeName \
            and int(self.blogPostLikeCountOld) + 1 == int(self.blogPostLikeCountNew):
            logging.info('=============点赞成功=============')
            return True
        else:
            logging.error('点赞失败')
            self.getScreenShot('云医圈界面-点赞')
            self.find_elements(*self.blogPostContent2_text)[0].click()
            time.sleep(3)
            self.getScreenShot('帖子详情界面-点赞')
            self.find_element(*self.blogPostDetailsLike_button).click()
            time.sleep(3)
            self.getScreenShot('点赞人列表界面-点赞')

            self.find_element(*self.blogPostBack_button).click()
            time.sleep(3)
            self.find_element(*self.blogPostBack_button).click()


    # 回复
    def blogPostReply(self, replyContent):
        self.cloudDEachPageView(0)
        logging.info('=============点击全部界面=============')
        self.find_element(*self.cloudDPageAll_button).click()

        self.blogPostReplyComment = replyContent
        self.blogPostReplyCountOld = self.find_elements(*self.blogPostReplyCount_text)[0].text

        logging.info('=============回复评论=============')
        self.find_elements(*self.blogPostReply_button)[0].click()
        self.find_element(*self.blogPostReplyComment_input).send_keys(replyContent)
        self.find_element(*self.blogPostReplySendComment_button).click()

        logging.info('=============获得评论内容=============')
        self.blogPostReplyCountNew = self.find_elements(*self.blogPostReplyCount_text)[0].text

        self.blogPostReplyName = (self.find_elements(*self.blogPostReplyName_text)[0].text)[:-1]
        self.blogPostReplyContent = self.find_elements(*self.blogPostReplyContent_text)[0].text

        logging.info('=============获得帖子详情内的评论内容=============')
        self.find_elements(*self.blogPostContent2_text)[0].click()
        time.sleep(3)
        self.blogPostDetailsReplyName = self.find_elements(*self.blogPostDetailsReplyName_text)[1].text
        # self.blogPostDetailsReplyName = self.find_elements(*self.blogPostDetailsReplyName_text)
        # print(self.blogPostDetailsReplyName)
        self.blogPostDetailsReplyContent = self.find_elements(*self.blogPostDetailsReplyContent_text)[0].text

        self.find_element(*self.blogPostBack_button).click()


    def check_blogPostReply(self):
        logging.info('=============我的界面的用户名：%s=============' % self.mineName)
        logging.info('=============云医圈的用户名：%s=============' % self.blogPostReplyName)
        logging.info('=============帖子详情的用户名：%s=============' % self.blogPostDetailsReplyName)

        logging.info('=============输入的评论内容：%s=============' % self.blogPostReplyComment)
        logging.info('=============云医圈的评论内容：%s=============' % self.blogPostReplyContent)
        logging.info('=============帖子详情的评论内容：%s=============' % self.blogPostDetailsReplyContent)

        # logging.info('=============旧的回复数量：%s=============' % self.blogPostReplyCountOld)
        # logging.info('=============新的回复数量：%s=============' % self.blogPostReplyCountNew)

        if self.blogPostReplyComment == self.blogPostReplyContent == self.blogPostDetailsReplyContent \
            and self.mineName == self.blogPostReplyName == self.blogPostDetailsReplyName: \
            # and int(self.blogPostReplyCountOld) + 1 == int(self.blogPostReplyCountNew):
            logging.info('=============回复成功=============')
            return True
        else:
            logging.error('回复失败')
            self.getScreenShot('云医圈界面-回复评论')
            self.find_elements(*self.blogPostContent2_text)[0].click()
            time.sleep(3)
            self.getScreenShot('帖子详情界面-回复评论')
            self.find_element(*self.blogPostBack_button).click()


    # 删除回复
    def blogPostReplyDel(self):
        self.cloudDEachPageView(0)
        logging.info('=============点击全部界面=============')
        self.find_element(*self.cloudDPageAll_button).click()

        logging.info('=============删除回复=============')
        self.blogPostReplyCountOld = self.find_elements(*self.blogPostReplyCount_text)[0].text
        self.find_elements(*self.blogPostContent2_text)[0].click()

        try:
            self.find_elements(*self.blogPostDetailsReplyContent_text)
        except NoSuchElementException:
            logging.info('=============没有回复=============')
            return False
        else:

            name = []
            name_list = self.find_elements(*self.blogPostDetailsReplyName_text)
            for i in range(len(name_list)):
                name.append(self.find_elements(*self.blogPostDetailsReplyName_text)[i].text)

            if self.mineName in name[1:]:
                for i in range(len(name[1:])):
                    if (name[1:])[i] == self.mineName:
                        i += 1
                        logging.info('=============点击删除回复=============')
                        self.find_elements(*self.blogPostDetailsReplyName_text)[i].click()
                        self.find_elements(*self.blogPostDetailsReplyBut_button)[0].click()
                        break

            else:
                logging.info('=============没有对应的评论=============')
                return False

            self.find_element(*self.blogPostBack_button).click()
            self.blogPostReplyCountNew = self.find_elements(*self.blogPostReplyCount_text)[0].text


    def check_blogPostReplyDel(self):
        logging.info('=============旧的回复数量：%s=============' % self.blogPostReplyCountOld)
        logging.info('=============新的回复数量：%s=============' % self.blogPostReplyCountNew)
        if int(self.blogPostReplyCountOld) - 1 == int(self.blogPostReplyCountNew):
            logging.info('=============删除回复成功=============')
            return True
        else:
            logging.error('删除回复失败')
            self.getScreenShot('云医圈-删除回复')
            self.find_elements(*self.blogPostContent2_text)[0].click()
            time.sleep(3)
            self.getScreenShot('帖子详情-删除回复')
            self.find_element(*self.blogPostBack_button).click()
            return False


    # 收藏
    def blogPostCollect(self):
        logging.info('=============获得收藏列表=============')
        self.find_elements(*self.mineImage_button)[3].click()

        logging.info('=============获得收藏列表中的内容=============')
        try:
            self.find_elements(*self.blogPostContent_text)
        except NoSuchElementException:
            logging.info('=============获得收藏列表没有内容=============')
            self.getScreenShot('未找到元素')
        else:
            self.blogPostContentOld = self.find_elements(*self.blogPostContent_text)[0].text
            if len(self.blogPostContentOld) > 10:
                self.blogPostContentOld = self.blogPostContentOld[:10]

        self.find_element(*self.blogPostBack_button).click()
        self.cloudDEachPageView(0)

        logging.info('=============获得帖子内容=============')
        self.blogPostContentNew = self.find_elements(*self.blogPostContent_text)[0].text
        if len(self.blogPostContentNew) > 10:
            self.blogPostContentNew = self.blogPostContentNew[:10]

            if self.blogPostContentNew == self.blogPostContentOld:
                logging.info('=============已经收藏=============')
                self.find_elements(*self.blogPostMore_button)[0].click()
                self.find_element(*self.blogPostMoreCollect_button).click()
                self.find_element(*self.blogPostMoreCollect_button).click()
            else:
                logging.info('=============未收藏=============')
                self.find_elements(*self.blogPostMore_button)[0].click()
                self.find_element(*self.blogPostMoreCollect_button).click()

        self.find_element(*self.blogPostMoreCancel_button).click()


    def check_blogPostCollect(self):
        self.mineView()
        time.sleep(5)
        self.find_elements(*self.mineImage_button)[3].click()
        logging.info('=============获得收藏列表中的内容=============')
        try:
            self.find_elements(*self.blogPostContent_text)
        except NoSuchElementException:
            logging.info('=============获得收藏列表没有内容=============')
            self.getScreenShot('未找到元素')
        else:
            self.blogPostContentOld = self.find_elements(*self.blogPostContent_text)[0].text
            if len(self.blogPostContentOld) > 10:
                self.blogPostContentOld = self.blogPostContentOld[:10]

        logging.info('=============收藏列表中的内容：%s=============' % self.blogPostContentOld)
        logging.info('=============云医圈中的内容：%s=============' % self.blogPostContentNew)

        if self.blogPostContentOld == self.blogPostContentNew:
            logging.info('=============收藏成功=============')
            return True
        else:
            logging.error('收藏失败')
            self.getScreenShot('收藏列表-收藏')
            self.find_element(*self.blogPostMoreCancel_button).click()
            self.cloudDEachPageView(0)
            self.getScreenShot('云医圈-收藏')


    def login_cloudD(self):
        a = self.mineView()
        if a == True:
            logging.info('=============获得用户名=============')
            self.mineName = self.find_element(*self.mineName_text).text
            # self.cloudDEachPageView(0)
            return a
        else:
            return a

if __name__ == '__main__':
    driver = appium_desired()
    l = CloudDPage(driver)
    l.login_cloudD()
    # l.blogPostAttention()
    # l.check_blogPostAttention()

    l.blogPostLike()
    l.check_blogPostLike()

    # l.blogPostReply('hello')
    # l.check_blogPostReply()
    #
    # l.blogPostReplyDel()
    # l.check_blogPostReplyDel()
    #
    # l.blogPostCollect()
    # l.check_blogPostCollect()