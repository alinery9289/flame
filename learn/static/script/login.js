// JavaScript Document
function judgeUserid(inputid,textid){
	var value=document.getElementById(inputid).value;//获取input的内容
	var filter=/^s*[.A-Za-z0-9_-]{5,15}s*$/;
	if (value==""){
		document.getElementById(textid).innerHTML="用户名不能为空";
	}
	else {
		if (!filter.test(value)) { 
			document.getElementById(textid).innerHTML="用户名填写不正确,请重新填写！可使用的字符为（A-Z a-z 0-9 _ - .)长度不小于5个字符，不超过15个字符，注意不要使用空格。"; 
		} 
		else {
			document.getElementById(textid).innerHTML="";
//			document.getElementById("frgetpw").href="/medialabWebapp/rest/user/passwordreset/userid/"+value;
		}
	}
}

function judgePassword(inputid,textid){
	var value=document.getElementById(inputid).value;//获取input的内容
	var filter=/^s*[.A-Za-z0-9_-]{5,20}s*$/;
	if (value==""){
		document.getElementById(textid).innerHTML="密码不能为空";
	}
	else {
		if (!filter.test(value)) { 
			document.getElementById(textid).innerHTML="密码不正确,请重新填写！可使用的字符为（A-Z a-z 0-9 _ - .)长度不小于5个字符，不超过20个字符，注意不要使用空格。"; 
		} 
		else {document.getElementById(textid).innerHTML="";}
	}
}

function judgeUseridorEmail(uidorpw){
	var value=document.getElementById(uidorpw).value;//获取input的内容
	var filter1=/^s*[.A-Za-z0-9_-]{5,15}s*$/;
	var filter2=/[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9\.]+(\.(com|cn|org|edu|hk|gov|mil|net|tw))/;
	if (value==""){
		document.getElementById("useridnotes").innerHTML="用户名/邮箱不能为空";
	}
	else {
		if (!filter1.test(value) && !filter2.test(value)) { 
			document.getElementById("useridnotes").innerHTML="用户名/邮箱填写格式不正确,请重新填写！"; 
		} 
		else {
			document.getElementById("useridnotes").innerHTML="";
		}
	}
}

function judgeEmail(inputid,textid){
	var value=document.getElementById(inputid).value;//获取input的内容
	var filter=/[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9\.]+(\.(com|cn|org|edu|hk|gov|mil|net|tw))/;
	if (value==""){
		document.getElementById(textid).innerHTML="邮箱不能为空";
	}
	else {
		if (!filter.test(value)) { 
			document.getElementById(textid).innerHTML="邮箱格式不正确,请重新填写！"; 
		} 
		else {document.getElementById(textid).innerHTML="";}
	}
}

function checkpassword(){
	var value1=document.getElementById('check_reg_password').value;//获取input的内容
	var value2=document.getElementById('reg_password').value;//获取input的内容
	if (value1!=value2){
		document.getElementById('check_reg_passwordnotes').innerHTML="此次输入的密码与第一次输入不符";
	}
	else {document.getElementById('check_reg_passwordnotes').innerHTML="";
	}
}

function checkBeforeLogin(){
	var value1= document.getElementById("passwordnotes").innerHTML;
	var value2= document.getElementById("useridnotes").innerHTML;
	var value3=document.getElementById("userid").value;
	var value4=document.getElementById("password").value;
	if ( value1=="" && value2=="" &&value3!="" && value4!=""){
		return true;
	}
	else {
		alert("表单内容存在错误，请确认无误后再提交！");	
		return false;
	}
}

function checkBeforeReg(){
	var value1= document.getElementById("reg_passwordnotes").innerHTML;
	var value2= document.getElementById("reg_useridnotes").innerHTML;
	var value3=document.getElementById("reg_userid").value;
	var value4=document.getElementById("reg_password").value;
	var value5= document.getElementById("check_reg_passwordnotes").innerHTML;
	var value6= document.getElementById("reg_emailnotes").innerHTML;
	var value7=document.getElementById("reg_email").value;
	var value8=document.getElementById("check_reg_password").value;
	if ( value1=="" && value2=="" && value3!="" && value4!="" && value5=="" && value6=="" && value7!="" &&value8!=""){
		return true;
	}
	else {
		alert("表单内容存在错误，请确认无误后再提交！");
		return false;
	}
}

function checkBeforeResetpw(){
	var value1= document.getElementById("reg_passwordnotes").innerHTML;
	var value2= document.getElementById("reg_useridnotes").innerHTML;
	var value3=document.getElementById("reg_userid").value;
	var value4=document.getElementById("reg_password").value;
	var value5= document.getElementById("check_reg_passwordnotes").innerHTML;
	var value6=document.getElementById("check_reg_password").value;
	if ( value1=="" && value2=="" && value3!="" && value4!="" && value5=="" &&value6!=""){
		return true;
	}
	else {
		alert("表单内容存在错误，请确认无误后再提交！");
		return false;
	}
}

function checkBeforeGetpw(){
	var value1= document.getElementById("useridnotes").innerHTML;
	var value2=document.getElementById("uidorpw").value;
	if ( value1=="" && value2!="" ){
		getpw_form.action="/medialabWebapp/rest/user/passwordreset/userid/"+value2;
		return true;
	}
	else {
		alert("表单内容存在错误，请确认无误后再提交！");	
		return false;
	}
}

$(window).load(function() {
//	var value= document.getElementById("judgeloginornot").innerHTML;
//	if (value==""|| value=="null"){
//		document.getElementById("loginregdiv").style.display="inline";
//		document.getElementById("logineddiv").style.display="none";
//	}
//	else {
//		document.getElementById("loginregdiv").style.display="none";
//		document.getElementById("logineddiv").style.display="inline";
//		refreshUser(value);
//	}
//	var loginstate=document.getElementById("judgeloginstate").innerHTML;
//	if (loginstate!=""&& loginstate!="null"&& loginstate!="success"){
//		alert(loginstate);
//	}
});

function logout(){
	$.ajax({
        type : "DELETE",  
        url : "/medialabWebapp/rest/user/"
   });
}

function refreshUser(value){
	$.ajax({
        type : "GET",  
        url : "/medialabWebapp/rest/user/authcode/"+value,
        dataType: "xml",  
        success : function(data) { 
        	
        	$(data).find("userModel").each(function(i){  
        		var userid_value=$(this).children("userid").text(); //取文本
        		var userstorage_value=$(this).children("userstorage").text(); //取文本
	        	document.getElementById('logineduserdiv').innerHTML="<p style=\"color:#fff\">用户: "+userid_value +"&nbsp|&nbsp存储: "+userstorage_value+"/500.0M&nbsp|&nbsp</p>";
        	});
        	
        },
		error :  function() {  
           //do something 
        	document.getElementById('logineduserdiv').innerHTML="error" ;
        }
   });
}

//var imaRec_timeout= [];
var img_timer;
function gettalkword(imageId){
	$.ajax({
        type : "GET",  
        url : "/imagerec/imagerecstate/"+imageId,
        dataType: "text",  
        success : function(data) { 
        	if (data!="Processing"){
        		var imagerec_state=[];
        		imagerec_state=data.split("\n");
        		for (var i=0;i<imagerec_state.length-1;i++){
        			$('#imageInf').append($('<li>').text(imagerec_state[i]));
        		}
        		clearTimeout(img_timer);
//            	var fileIndex=$('#imageInf').find("li").length;
//    	        var fileNum=$('.upload_preview').find("div.upload_append_list").length;
//    	        if (fileIndex >= fileNum){
    	        $("#imageProcessState").text("Upload Successful! Processing Successful!");
//    	        }
        	}
        	else {
        		img_timer=setTimeout("gettalkword('"+imageId+"')",3000);
        	}
        },
		error :  function() {  
           //do something 
        }
   });
}



