<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-Transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
<title>Jacks�I�t�B�V�����t�@���N���u ����o�^</title>
<meta name="description" content="�V��v�� �g���v��K,Jacks �I�t�B�V�����t�@���N���u ����o�^,�W���b�N�X" />
<meta name="keywords" content="JacKs[�W���b�N�X]�I�t�B�V�����t�@���N���u�ɓ����]�̕��͂����炩��" />
<meta name="robots" content="noindex, nofollow, noarchive">
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />

<link rel="stylesheet" type="text/css" href="./css/common.css" />
<link rel="stylesheet" type="text/css" href="./css/share.css" />
<link rel="stylesheet" type="text/css" href="./css/jp/common_side.css" />



<style type="text/css">
#container #main #content section #contwrapp #registarea table tr td .front {
	font-size: 10px;
}
</style>
</head>
<body>

<div id="container" class="clear">
	<div id="header">
		<h1><img src="image/queens-top-main.jpg" alt="Jacks �I�t�B�V�����t�@���N���u ����o�^" width="900"/></a></h1>
	</div>
	<div id="main" class="clear">
		<div id="content" class="clear">
<?php

$list_r = array(
"sei" => "��",
"mei" => "��",
"sei2" => "��(�t���K�i)",
"mei2" => "��(�t���K�i)",
"nickname" => "�j�b�N�l�[��",
"email1" => "���[���A�h���X�P",
"email2" => "���[���A�h���X�Q",
"nickname" => "�j�b�N�l�[��",
"gender" => "����",
"birth_year" => "�N",
"birth_month" => "��",
"birth_day" => "��",
"czip" => "�X�֔ԍ��P",
"czip2" => "�X�֔ԍ��Q",
"pref" => "�s���{��",
"addr" => "�Z���P",
"addr2" => "�Z���Q",
"phone1" => "�d�b�ԍ��P",
"phone2" => "�d�b�ԍ��Q",
"pass1" => "�p�X���[�h",
"pass2" => "�p�X���[�h�m�F�p",
"mailmagazine" => "���[���}�K�W���̉�",
"ninki" => "�D���Ȑl"

);


if($_POST["register"] == "1"){






foreach($list_r as $key => $val){
${$key} = $_POST[$key];
/*if(${$key} == ""){
echo $error[$key] = $val."�����͂���Ă��܂���<br />";
$error_checker = 1;
}*/
}

if(substr($pass1,5,1) == "" ){
$error["pass1"] = "<font color='red'>�p�X���[�h�͂U�����ȏ�ł��B</font><br />";
}
if($pass1 != $pass2){
$error["pass2"] = "<font color='red'>�p�X���[�h�m�F�p���}�b�`���Ă��܂���B</font><br />";
}

/*
$list_nr = array(

);
foreach($list_r as $key => $val){
${$key} = $_POST[$key];
}
}
*/
if(!isset($error["pass1"]) && !isset($error["pass2"])){
   mb_language('ja');
   mb_internal_encoding("Shift-JIS");
 
   $from = 'queens@triple-kmen.com'; 
   $reply_to = 'queens@triple-kmen.com'; 
   $to = $email1;
   $header = "From: $from\n";  
   $header .= "Reply-To: $reply_to\n";
   $header .= "X-Mailer: myphpMail ". phpversion(). "\n"; 
   $subject = "Jacks�t�@���N���u�o�^����"; 
   $message = "JacKs�I�t�B�V�����t�@���N���u�����ǂł������܂��B

���葱�����肪�Ƃ��������܂��B
�t�@���N���u������o�^�������v���܂����B

���萔�ł����A���L�̋��z���w��̐U����܂�
�������̒���낵�����肢�v���܂��B


[ �t�@���N���u��� �N��� ]

�N���F��3,000

��������������������

2012/6/7�܂ł̂������Ȃ�
�N���F��2,500




[ �U���� ]

�������M�p�g�� �{�X�c�ƕ� ���� 0167183  
(��)�h�A�E�}�E���h




JacKs�I�t�B�V�����t�@���N���u������


";
   
   mb_send_mail($to, $subject, $message, $header); 


 $to = "queens@triple-kmen.com";
   $header = "From: $from\n";  
   $header .= "Reply-To: $reply_to\n";
   $header .= "X-Mailer: myphpMail ". phpversion(). "\n"; 
   $subject = "Jacks�t�@���N���u�o�^�����ʒm"; 
   $message = "���L�̓o�^������܂����B

#####�o�^���e#####
";

foreach($list_r as $key => $val){
	$message .= "��".$val."
".${$key}."

";
}


   
   mb_send_mail($to, $subject, $message, $header); 

}

}

if(!isset($error["pass1"]) && !isset($error["pass2"]) && $_POST["register"] == 1){

?>



		<h2 class="sh_heading_main_b"><span>�t�@���N���u����o�^���������܂����B</span></h2>
<p><br />
				  <br />
				  <br />
				  ���o�^�A���肪�Ƃ��������܂��B<br />
				  JacKs�I�t�B�V�����t�@���N���u�ւ̓o�^�������������܂����B<br />
				  <br />
				</p>
				<ul>
				  �����ǂ���́uJacKs�t�@���N���u����o�^�������[���v�����m�F�̏�A<br />
				  JacKs�����ǎw��̌����܂ł��������������B
</ul>
				<p>  <br />
	    </p>


<?php }else{

if($_POST["register"] == ""){


foreach($list_r as $key => $val){
${$key} = "";
}

}

 ?>


<section>

<div id="contwrapp">




  <form action="./touroku.php" method="POST" id="registarea">
	<table width="600" border="0" cellpadding="0" cellspacing="0">
	  <tr>
	    <td><span class="registitem">�������O(�S�p)</span></td>
	    <td colspan="2"><span class="back">��</span>
	      <input name="sei" type="text" required="required" value="<?php echo $sei; ?>" size="15" maxlength="20" />
	      <span class="both">�@��</span>
	      <input name="mei" type="text" required="required" value="<?php echo $mei; ?>" size="15" maxlength="20" /></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">���t���K�i(�S�p)</span></td>
	    <td colspan="2"><span class="back">�Z�C</span>
	      <input name="sei2" type="text" required="required" value="<?php echo $sei2; ?>" size="15" maxlength="20" />
	      �@
				<span class="both">���C</span>
				<input name="mei2" type="text" required="required" value="<?php echo $mei2; ?>" size="15" maxlength="20" /></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">���j�b�N�l�[��(�S�p���p��)</span></td>
	    <td colspan="2"><input type="text" name="nickname" required="required" value="<?php echo $nickname; ?>" class="wtype4" id="nickname" onblur="checkNickName()" /></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">�����[���A�h���X1 (PC or �g��)</span></td>
	    <td colspan="2">
<?php if($_GET['jid'] != ""){	
echo urldecode($_GET['jid']); ?>
		<input type="hidden" name="email1" value="<?php echo urldecode($_GET['jid']); ?>"><?php }else{ ?>
<?php echo $email1; ?>
		<input type="hidden" name="email1" value="<?php echo $email1; ?>">
<?php } ?>
</td>
	    </tr>
	  <tr>
	    <td><span class="registitem">���[���A�h���X2 (PC or �g��)</span></td>
	    <td colspan="2"><input type="text" name="email2" value="<?php echo $email2; ?>" class="wtype5" /></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">������</span></td>
	    <td><input type="radio" name="gender" value="�j��" <?php if($gender == 2){ echo ' checked="checked" ';}?> />
	      <span class="back">�j��</span>
          <input type="radio" name="gender" value="����" <?php if($gender != 2){ echo ' checked="checked" ';}?> />
          ����</td>
	    <td>&nbsp;</td>
	    </tr>
	  <tr>
	    <td><span class="registitem">�����N����</span></td>
	    <td colspan="2"><input name="birth_year" type="text" required="required" class="wtype2" value="<?php echo $birth_year; ?>" size="10" maxlength="4" />
          <span class="back">�N</span>
          <input name="birth_month" type="text" required="required" class="wtype1" value="<?php echo $birth_month; ?>" size="4" maxlength="2" />
          <span class="back">��</span>
          <input name="birth_day" type="text" required="required" class="wtype1" value="<?php echo $birth_day; ?>" size="4" maxlength="2" />
          <span>��</span></td>
	    </tr>
	  <tr>
	    <td valign="top"><span class="registitem">���Z��</span></td>
	    <td colspan="2" nowrap="nowrap" class="back">�X�֔ԍ�
	      <input name="czip" type="text" required="required" id="czip" value="<?php echo $czip; ?>" size="5" maxlength="3" />
	      -
	      <input name="czip2" type="text" required="required" id="czip2" value="<?php echo $czip2; ?>" size="5" maxlength="4" />
	      <br />
�s���{��
<input type="text" name="pref" required="required" value="<?php echo $pref; ?>" id="pref2" />
<br />
<span class="registitem"></span>�s�撬��
<input type="text" name="addr" required="required" value="<?php echo $addr; ?>" class="wtype4" id="addr2" />
<span class="front">(��)�V�h���v��</span><br />
<span class="registitem"></span>�Ԓn/������(�S�p)
<input type="text" name="addr2" required="required" value="<?php echo $addr2; ?>" class="wtype5" />
<span class="front">(��)1-12-4 ASS��2�r��5F</span></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">���A����d�b�ԍ�1(���� or �g��)</span></td>
	    <td colspan="2"><input type="text" name="phone1" required="required" value="<?php echo $phone1; ?>" class="wtype4" />	      <span class="front">(��)���p�����A�n�C�t���Ȃ�</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">�A����d�b�ԍ�2(���� or �g��)</span></td>
	    <td colspan="2"><input type="text" name="phone2" value="<?php echo $phone2; ?>" class="wtype4" />	      <span class="front">(��)���p�����A�n�C�t���Ȃ�</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">���p�X���[�h</span></td>
	    <td colspan="2"><?php if(isset($error["pass1"])){echo $error["pass1"]; } ?><input type="password" name="pass1" required="required" value="" />	      <span class="front">��6���ȏ�̔��p�p����</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">���p�X���[�h�m�F�p</span></td>
	    <td colspan="2"><?php if(isset($error["pass2"])){echo $error["pass2"]; } ?><input type="password" name="pass2" required="required" value="" />	      <span class="front">��6���ȏ�̔��p�p����</span></td>
	    </tr>


	  <tr>
	    <td><span class="registitem">��JacKs�ň�ԍD���Ȑl�͒N�ł����H</span></td>
	        <td colspan="2"><input type="radio" name="ninki" value="�C�E�V�q����" <?php if($ninki == "�C�E�V�q����"){ echo ' checked="checked" ';}?> />
	      <span class="back">�C�E�V�q����</span>
	      <input type="radio" name="ninki" value="�~�b�L�[" <?php if($ninki == "�~�b�L�["){ echo ' checked="checked" ';}?>/>
	      <span class="back">�~�b�L�[</span>
          <input type="radio" name="ninki" value="�i�E�N��"  <?php if($ninki == "�i�E�N��"){ echo ' checked="checked" ';}?>/>
	      <span class="back">�i�E�N��</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">�����[���}�K�W��</span></td>
	    <td colspan="2"><input type="radio" name="mailmagazine" value="��M����" <?php if($mailmagazine == 1){ echo ' checked="checked" ';}?> />
	      <span class="back">��M����@</span>
	      <input type="radio" name="mailmagazine" value="��M���Ȃ�" <?php if($mailmagazine != 1){ echo ' checked="checked" ';}?>/>
	      ��M���Ȃ�</td>
	    </tr>
	  </table>
	<br />
	<br />
   <fieldset>
     <p>
<input type="hidden" name="register" value="1">
       <input type="submit" value="���M����">
   </p>
</fieldset>
   </form>


 </div>
  
</section>
<?php } ?>
		</div>
	</div><!-- /main -->
		<div id="menu">
		<div class="sh_menu">
        	<p class="sh_menu_list"><a href="index.php" title="����o�^�g�b�v">����o�^�g�b�v</a></p>
			<p class="sh_menu_list"><a href="index.php#tokuten" title="������T">������T</a></p>
			<p class="sh_menu_list"><a href="index.php#kiyaku" title="���p�K��">���p�K��</a></p>
			<p class="sh_menu_list"><a href="http://triple-kmen.com/" title="�g���v��K�g�b�v">�g���v��K�g�b�v</a></p>
		</div>
	</div><!-- /menu -->
<div><img src="image/footer.gif" width="900" height="170" align="right"></div>
</div><!-- /container -->

<!-- /display:none�^�O -->
</body>
</html>
