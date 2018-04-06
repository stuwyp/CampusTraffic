var reg = '<form ><div id="name"><label>' +
    '<span> 登录名：</span>' +
    '<input type="text" class="text"/>' +
    '<p class="msg"><i class="ati"></i>5-25个字符，一个汉字为两个字符</p></label></div>' +
    '<div><label><span><b id = "count">0个字符</b></span></label></div>' +

    '<div ><label><span><b id = "count">0个字符</b></span></label></div>' +
    '<div id="pwd"><label><span>登录密码：</span><input type="password" class="text"</label><p class="msg" ><i class="err"></i>数字、字母（不分大小写）、汉字、下划线</p></div>' +
    '<div id="strength" style="margin:3px 0 10px 0"><label><span></span><em class="inactive">弱</em><em class="inactive">中</em><em class="inactive">强</em></label></div>' +

    '<div id="pwd2" style="margin-bottom:20px "><label><span>确认密码：</span><input type="password" class="text" disabled=""/></label><p class="msg" ><i class="ati"></i>请再输入一次</p></div>' +

    '<div id="check"><label><span>验证码:</span><input type="text" style="width:50px"/><img src="" width = "100" height="30"/><a class="changing" href="" title="重新获取验证码"></a></label></div>'
    + '<div id="register"><input id="submitid" type="submit" value="注册"></div>' + '<div id="recall" class="recall"><input type="button" value="取消"></div>' +
    '</form>';

var reg_name = '<div class="loginCon"><div id="Hlog">注册</div><div id="close"></div></div>';

function openMask(reg_name, reg, fn) {
    //获取页面的高度
    var sHeight = document.documentElement.scrollHeight;
    var sWidth = document.documentElement.scrollWidth;

    //可视区域的高宽
    //如果页面是一个竖向的页面，则可视区域的宽度和页面一致
    var wHeight = document.documentElement.clientHeight;


    var oMask = document.createElement("div");
    oMask.id = "mask";
    oMask.style.height = sHeight + "px";
    oMask.style.width = sWidth + "px";
    document.body.appendChild(oMask);


    var oLogin = document.createElement("div");
    oLogin.id = "login";
    oLogin.innerHTML = reg_name + reg;
    document.body.appendChild(oLogin);
    var dHeight = oLogin.offsetHeight;
    var dWidth = oLogin.offsetWidth;
    oLogin.style.left = (sWidth - dWidth) / 2 + "px";
    oLogin.style.top = (wHeight - dHeight) / 2 + "px";

    if (fn) {
        fn();
    }


    var oClose = document.getElementById("close");
    var recall = document.getElementsByClassName("recall")[0];
    oMask.onclick = oClose.onclick = recall.onclick = function () {
        document.body.removeChild(oMask);
        document.body.removeChild(oLogin);

    }

}


//与注册页面的控制

function getLength(str) {

    return str.replace(/[^\x00-xff]/g, "xx").length;

}

function findStr(str, n) {
    var tmp = 0;
    for (var i = 0; i < str.length; i++) {

        if (str.charAt(i) == n) {
            tmp++;
        }
    }
    return tmp;

}


function interact_reg() {
    var alinput = document.getElementsByClassName("text");
    var oName = alinput[0];
    var pwd = alinput[1];
    var pwd2 = alinput[2];
    var aP = document.getElementsByClassName("msg");
    var name_msg = aP[0];
    var pwd_msg = aP[1];
    var pwd2_msg = aP[2];
    var count = document.getElementById("count");
    var aEm = document.getElementsByTagName("em");
    var name_length = 0;


    //\ue400-\u9fa5    为中文的Unicode码

    //匹配用户名


    //用户名
    oName.onfocus = function () {
        name_msg.style.display = "inline-block";

    }

    oName.onkeyup = function () {

        count.style.visibility = "visible";
        name_length = getLength(this.value);
        count.innerHTML = name_length + "个字符";
        if (name_length == 0) {
            count.style.visibility = "hidden";

        }


    }

    oName.onblur = function () {
        //含有非法字符
        //不能为空
        //长度不能超过25个字符
        //正确
//    var  re  = /[^\w\ue400-\u9fa5]/g;
//    if(re.test(this.value)){
//        name_msg.innerHTML = '<i class="err"></i>含有非法字符！'
//
//    }
        if (this.value == "") {

            name_msg.innerHTML = '<i class="err"></i>不能为空！'
        }

        else if (name_length > 25) {
            name_msg.innerHTML = '<i class="err"></i>不能超过25个字符！'

        }
        else if (name_length < 5) {
            name_msg.innerHTML = '<i class="err"></i>不能少于5个字符！'
            pwd.setAttribute("disabled", "");

        }
        else {

            name_msg.innerHTML = '<i class = "ok">&nbsp;&nbsp;OK!';
        }


    };

    //密码

    pwd.onfocus = function () {

        aEm[0].className = "active";
        pwd_msg.style.display = "inline-block";
        pwd_msg.innerHTML = '<i class = "ati"></i>6-16个字母加数字或符号的组合密码';
    }

    //大于5 个字符为中
    //大于10个字符为强
    pwd.onkeyup = function () {
        if (this.value.length > 5) {
            aEm[1].className = "active";
            pwd2.removeAttribute("disabled");
            pwd2_msg.style.display = "inline-block";

        }
        else {
            aEm[1].className = "";
            pwd2.setAttribute("disabled", "disabled");
            pwd2_msg.style.display = "none";

        }
        //密码为强
        if (this.value.length > 10) {
            aEm[2].className = "active";
        }
        else {
            aEm[2].className = "";

        }


    }

    pwd.onblur = function () {

        var m = findStr(pwd.value, pwd.value[0]);
        var re_n = /[^\d]/g;
        var re_t = /[^a-zA-Z]/g;
        //甭能为空
        if (this.value == "") {
            pwd_msg.innerHTML = '<i class="err"></i>不能为空！'
        }
        //不能用相同字符
        else if (m == this.value.length) {
            pwd_msg.innerHTML = '<i class="err"></i>不能全使用相同字符！'
        }
        //长度为6-16
        else if (this.value.length < 6 || this.value.length > 16) {

            pwd_msg.innerHTML = '<i class="err"></i>不能少于6个或是多与=于16个字符'
        }
        //不能全为数字
        else if (!re_n.test(this.value)) {
            pwd_msg.innerHTML = '<i class="err"></i>不能全为数字';
        }
        else if (!re_t.test(this.value)) {
            pwd_msg.innerHTML = '<i class="err"></i>不能全为字母';
        }
        else {
            pwd_msg.innerHTML = '<i class="ok"></i>OK';
        }


        //不能全为字母
        //ok


    };

    //确认密码


    pwd2.onkeyup = function () {

        if (this.valued == "") {
            pwd2_msg.innerHTML = '<i class="ati"></i>再输入一次';
        }


    }
    pwd2.onblur = function () {


        if (this.value != pwd.value) {

            pwd2_msg.innerHTML = '<i class="err"></i>两次的密码输入不一致';
        }
        else if (this.value == "") {
            pwd2_msg.innerHTML = '<i class="ati"></i>再输入一次';

        }
        else {
            pwd2_msg.innerHTML = '<i class="ok"></i>&nbsp;&nbsp;ok';

        }


    }


}

// 登录界面

var log = '<form >' +
    '<div id="log_name"><label>' +
    '<span> 登录名：</span>' +
    '<input type="text" class="text"/></div>' +
    '<div id="log_pwd"><label><span>登录密码：</span><input type="password" class="text"</label></div>' +
    '<div id="log"><input type="submit" value="登录"></div>' + '<div id="log_recall" class="recall" ><input type="button" value="取消"></div>'
'</form>';


var log_name = '<div class="loginCon"><div id="Hlog">登录</div><div id="close"></div></div>';















