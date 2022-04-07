from bs4 import BeautifulSoup
import requests
def spider():
    url = 'https://3g.163.com/money/article/G5BCQT5S002580S6.html' 
    response = requests.get(url=url)
    res = response.text
    soup = BeautifulSoup(res,'html.parser',from_encoding='utf-8')
    body = soup.find("div",class_="article-content")
    html1 = (        "<!DOCTYPE html>\n" +
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
    html2 =(" <div class=\"comment_box\">\n" +
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
        "            var address = \"https://3g.163.com/money/article/G5BCQT5S002580S6.html\"\n" +
        "            var comments = $(\"#input_kw\").val()\n" +
        "            // alert(comments)\n" +
        "            $.ajax({\n" +
        "                url: \"http://localhost:5000/getcomments\",\n" +
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
        "                alert(\"hellow\")\n" +
        "            })\n" +
        "        })\n" +
        "    </script>\n" +
        "</body>\n" +
        "\n" +
        "\n" +
        "\n" +
        "</html>")
    with open('./news2.html','w',encoding='utf-8') as fp:
        fp.write(html1+str(body)+html2)