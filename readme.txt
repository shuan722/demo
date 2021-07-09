github :DNS工具查询 https://tool.chinaz.com/dns/


pycharm 使用git步骤记录
1. 初始化文件 git init
2. 配置remote  git remote add origin https://xxxxx 关联远程仓库并配置
    git remote -v 查看远程配置信息
3. 创建文件并提及交到存储区
   git add  提交到缓存区
   git commit	从缓存区到暂存区,并加入-m备注
4. git push -u oragin master	提交代码到远程仓库

5. 开发人员远程库clone项目
    1. vcs - git - clone
    2.开发人员修项目代码,
        git add  / git commit -m
    3. 开发人员push操作

6. 项目经理pull代码

7. 代码冲突问题
    1. 出现冲突如何解决
	2. 如何避免冲突, 先pull代码后在更新代码,及时更新
	3. 出现代码冲突及时沟通,不要相互覆盖