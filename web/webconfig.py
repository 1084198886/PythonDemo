from flask import Flask, url_for, request, redirect, abort

"""
flask使用
"""
app = Flask(__name__)


def config_flask():
    """参数配置"""
    # app.config['DEBUG'] = True  # 手动设置配置
    app.config.from_object('config')  # 以模块名加载配置文件
    # app.config.from_pyfile('config.py', silent=False)  # 以文件名加载配置文件


config_flask()


# @app.route('/item/1/', methods=['GET'])
@app.route('/item/<int:id>/', methods=['GET'])
def item(id):
    """
    URL规则
    :param id:
    :return: http响应内容
    知识点：1,此方法使用注解@app.route标识请求路径，路径名称使用<参数类型:参数名称>标识动态参数
    """
    return 'Item:{}'.format(id)


with app.test_request_context():
    """
    构造URL
    """
    print("url_for: ", url_for('item', id=1, next='2'))

'''
以下是构造URL的示例
知识点： request，request.headers，request.form，request.args，redirect方法使用
'''


@app.route('/people/', methods=['GET'])
def pepople():
    name = request.args.get('name')
    print('request.args.name:', name)
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name:{} User-Agent:{}'.format(name, user_agent)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    print('login method:', request.method)
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        print('user_id=', user_id)
        return 'User:{} login'.format(user_id)
    else:
        return 'Open login page'


@app.route('/secret/')
def secret():
    abort(401)  # abort 放弃请求，禁止访问
    return 'This is never executed !'


if __name__ == '__main__':
    app.run()
