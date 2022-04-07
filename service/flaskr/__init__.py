import os
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import render_template
import json
from . import db
## 数据库实例的创建
## 利用工厂模式去创建flask这个实例


## https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
## 用sqlite不需要你去搭建另外的数据库服务器


## 工厂模式 是一个很常用的用于创建对象的设计模式

## 用户资料endpoint
# R: Read 读取创建的user profile /GET
# C: Create 创建一个user profile /POST
# U: Update 更新创建的user profile /PUT
# D: Delete 删除创建的user profile /DELETE

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    db.init_app(app)

    def query_db(query, args=(), one=False):
        cur = db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from bs4 import BeautifulSoup
    import requests
    # 爬取网易的数据进行拼接
    def spider(url):
        url = url
        response = requests.get(url=url)
        res = response.text
        soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
        body = soup.find("div", class_="article-content")
        html1 = ("<!DOCTYPE html>\n" +
                 "<html lang=\"en\">\n" +
                 "\n" +
                 "<head>\n" +
                 "    <meta charset=\"UTF-8\">\n" +
                 "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\">\n" +
                 "    <title>Document</title>\n" +
                 "    <script src=\"https://code.jquery.com/jquery-3.0.0.min.js\"></script>\n" +
                 "    <style type=\"text/css\">\n" +
                 "        body {\n" +
                 "            margin-left: 12px;\n" +
                 "            margin-right: 12px;\n" +
                 "        }\n" +
                 "\n" +
                 "        .comment_box {\n" +
                 "            height: 1000px;\n" +
                 "            margin-top: 40px;\n" +
                 "            margin-bottom: 20px;\n" +
                 "        }\n" +
                 "\n" +
                 "        .comment_box .comment_list {\n" +
                 "            height: 400px;\n" +
                 "            margin-top: 40px;\n" +
                 "            margin-bottom: 20px;\n" +
                 "            padding-top: 10px;\n" +
                 "            padding-bottom: 10px;\n" +
                 "\n" +
                 "        }\n" +
                 "\n" +
                 "        .comment_box .comment_list .comment_list_default {\n" +
                 "            text-align: center;\n" +
                 "            font-size: 2em;\n" +
                 "        }\n" +
                 "\n" +
                 "        .comment_box .comment_list .comment_items {\n" +
                 "            margin-top: 5px;\n" +
                 "            margin-bottom: px;\n" +
                 "            border-bottom: ridge\n" +
                 "        }\n" +
                 "    </style>\n" +
                 "</head>\n" +
                 "\n" +
                 "<body>")
        html2 = (" <div class=\"comment_box\">\n" +
                 "        <div>\n" +
                 "            <p style=\"font-size:2em\"><b>评论区</b></p>\n" +
                 "            <textarea id=\"input_kw\" style=\"width: 100%;height: 66px;\" type=\"text\"></textarea>\n" +
                 "            <button id=\"sub_btn\" style=\"margin-top: 4px;float: right;\">发表评论</button>\n" +
                 "        </div>\n" +
                 "\n" +
                 "        <div class=\"comment_list\">\n" +
                 "            没有什么显示的\n" +
                 "            <!-- <div class=\"comment_list_default\">\n" +
                 "                \n" +
                 "            </div>    -->\n" +
                 "        </div>\n" +
                 "    </div>\n" +
                 "    <script>\n" +
                 "// 根据地址获取评论的函数\n" +
                 "        function getdata() {\n" +
                 "            var address = \""+url+"\"\n" +
                 "            var comments = $(\"#input_kw\").val()\n" +
                 "            // alert(comments)\n" +
                 "            $.ajax({\n" +
                 "                url: \"http://192.168.0.106:5000/getcomments\",\n" +
                 "                dataType: \"json\",\n" +
                 "                data: {\n" +
                 "                    address: address,\n" +
                 "                    comments: comments\n" +
                 "                },\n" +
                 "                success: function (data) {\n" +
                 "\n" +
                 "                    $(\".comment_list\").html(\"\")\n" +
                 "                    if (data[0].success === '成功') {\n" +
                 "                        for (let i = 1; i < data.length; i++) {\n" +
                 "                            var str = `        <div class=\"comment_items\">\n" +
                 "                                                    ${data[i].comments}\n" +
                 "                                                 \n" +
                 "                                                    </div>`\n" +
                 "                            // data[i].comments\n" +
                 "                            // console.log(str)\n" +
                 "                            $(\".comment_list\").append(str)\n" +
                 "                        }\n" +
                 "                    }\n" +
                 "\n" +
                 "                }\n" +
                 "\n" +
                 "            })\n" +
                 "        }\n" +
                 "\n" +
                 "\n" +
                 "        $(function () {\n" +
                 "            getdata()\n" +
                 "            $(\"#sub_btn\").on(\"click\", function () {\n" +
                 "                getdata()\n" +
                 "            })\n" +
                 "        })\n" +
                 "    </script>\n" +
                 "</body>\n" +
                 "\n" +
                 "\n" +
                 "\n" +
                 "</html>")
        with open('./flaskr/templates/index.html', 'w', encoding='utf-8') as fp:
            fp.write(html1 + str(body) + html2)

    # 将前端请求的地址返回，包含评论
    @app.route('/index',methods=["GET","POST","PUT","DELETE"])
    def index():
        url=request.args.get('url',1)
        # if request.method == 'POST':
        #     address = request.json.get('address')\
        #     print(request.args.get('address'))
        spider(url)
        return render_template('index.html')

    # h5中的ajax获取评论的请求
    @app.route('/getcomments', methods=["GET","POST","PUT","DELETE"])
    def getcomments():
        address = request.args.get('address')
        comments = request.args.get('comments')
        if(comments != ''):
            query = "INSERT INTO comments (comment,address) values('{}','{}')".format(comments,address)
            connection = db.get_db()
            cursor = connection.execute(query)
            connection.commit()
        query = "SELECT * FROM comments WHERE address= '{}'".format(address)
        result = query_db(query,one=False)
        (jsonify({'code': 0,'data':'DSB'}))

        if result: 
            # 打包成json
            data = [{'success':'成功'}]
            for res in result:
                dic = {'address':res['address'],'comments':res['comment'],}
                data.append(dic)
            response = make_response(json.dumps(data,ensure_ascii=False))
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Method'] = '*'
            response.headers['Access-Control-Allow-Headers'] = '*'
            return response
            # 没有查询到
        else: 
            data = [{'success':'失败'}]
            response = make_response(json.dumps(data,ensure_ascii=False))
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Method'] = '*'
            response.headers['Access-Control-Allow-Headers'] = '*'
            return response

    # 获取用户的请求
    @app.route('/user', methods=["GET","POST","PUT","DELETE"])
    def user():
        # if request.method == 'GET':
           
        #     uid = request.args.get('uid',1)
          
        #     query = "SELECT * FROM userProfile WHERE id = {}".format(uid)
         
        #     result = query_db(query,one=True)

        #     if result is None:
        #         return dict(message="user doesn't exist")
        #     else:
        #         username=result['username']
        #         fans=result['fans']
        #         print(result['username'])
        #         print(result['fans'])
        #         return dict(username=username,fans=fans)
        if request.method =='POST':
            print(request.json)
            uid = request.json.get('uid')
            pwd = request.json.get('pwd')
            status = request.json.get('status')
            
            if status=="register":
                connection = db.get_db()
                query = "INSERT INTO user (userID,pwd) values('{}','{}')".format(uid,pwd)
                print(query)
                try:
                    cursor = connection.execute(query)
                    connection.commit()
                    return jsonify([{'success':'True','message':'插入成功','errorcode':'0'}])
                except:
                    return jsonify([{'success':'Fail','message':'用户存在','errorcode':'1'}])
            if status == "login":
                connection = db.get_db()
                query = "SELECT * FROM user WHERE userID = {} and pwd ={}".format(uid,pwd)
                result = query_db(query,one=False)
                if result:

                    connection.commit()
                    return jsonify([{'success':'True','message':'查到用户，且密码正确','errorcode':'0'}])
                else:
                    return jsonify([{'success':'Fail','message':'用户，或密码错误','errorcode':'1'}])
        # elif request.method == 'PUT':         
        #     return '1'
        # elif request.method =='DELETE':
        #     # delete
        #     uid=request.args.get('uid',1)
        #     connection = db.get_db()
        #     query = "delete from userProfile where id = {}".format(uid)
        #     connection.execute(query)
        #     connection.commit()
        #     return dict(success=True)

    # 获取用户收藏的api
    @app.route('/userProfile', methods=["GET","POST","PUT","DELETE"])
    def userProfile():
        # 通过uid查询数据库的收藏
        if request.method == 'GET':  
            userID = request.args.get('userID',1)    
            print(userID)
            query = "SELECT * FROM userProfile WHERE userID = {}".format(userID)
            result = query_db(query,one=False)
             # 查询到
            if result: 
                # 打包成json
                data = [{'success':'True'}]
                for res in result:
                    dic = {'address':res['addres'],'NewsImage':res['NewsImage'],'NewsTitle':res['NewsTitle'],'Source':res['Source'],}
                    data.append(dic)
                return json.dumps(data)
            # 没有查询到
            else: return jsonify([{'success':'Fail'}])

        # 接受android发送的数据
        if request.method =='POST':
            print(request.json)
            uid = request.json.get('uid')
            address = request.json.get('address')
            NewsImage = request.json.get('NewsImage')
            NewsTitle = request.json.get('NewsTitle')
            Source = request.json.get('Source')
            connection = db.get_db()
            query = "INSERT INTO userProfile (userID,addres,NewsImage,NewsTitle,Source) values('{}','{}','{}','{}','{}')".format(uid,address,NewsImage,NewsTitle,Source)
            print(query)
            try:
                cursor = connection.execute(query)
                connection.commit()
                return jsonify([{'success':'True','message':'插入成功','errorcode':'0'}])
            except:
                return jsonify([{'success':'Fail','message':'插入失败','errorcode':'1'}])
        # elif request.method == 'PUT':         
        #     return '1'
        # elif request.method =='DELETE':
        #     # delete
        #     uid=request.args.get('uid',1)
        #     connection = db.get_db()
        #     query = "delete from userProfile where id = {}".format(uid)
        #     connection.execute(query)
        #     connection.commit()
        #     return dict(success=True)
    return app

    # venv\Scripts\activate
    # set FLASK_APP=flaskr
    # set FLASK_ENV=development
    # flask run
    # flask run --host=0.0.0.0
    # https://3g.163.com/touch/reconstruct/article/list/BD2AC4LMwangning/0-20.html
    # http://192.168.0.100/