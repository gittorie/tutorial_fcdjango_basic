from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser',
                               on_delete=models.CASCADE, # 글쓴이 탈퇴 >>> 해당 게시글 삭제
                                verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록일')
    
    # title 반환함
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글' # 패스트캠퍼스 게시글s 로 안뜨게 함
