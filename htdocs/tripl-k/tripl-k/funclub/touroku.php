<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-Transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
<title>Jacksオフィシャルファンクラブ 会員登録</title>
<meta name="description" content="新大久保 トリプルK,Jacks オフィシャルファンクラブ 会員登録,ジャックス" />
<meta name="keywords" content="JacKs[ジャックス]オフィシャルファンクラブに入会希望の方はこちらから" />
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
		<h1><img src="image/queens-top-main.jpg" alt="Jacks オフィシャルファンクラブ 会員登録" width="900"/></a></h1>
	</div>
	<div id="main" class="clear">
		<div id="content" class="clear">
<?php

$list_r = array(
"sei" => "姓",
"mei" => "名",
"sei2" => "姓(フリガナ)",
"mei2" => "名(フリガナ)",
"nickname" => "ニックネーム",
"email1" => "メールアドレス１",
"email2" => "メールアドレス２",
"nickname" => "ニックネーム",
"gender" => "性別",
"birth_year" => "年",
"birth_month" => "月",
"birth_day" => "日",
"czip" => "郵便番号１",
"czip2" => "郵便番号２",
"pref" => "都道府県",
"addr" => "住所１",
"addr2" => "住所２",
"phone1" => "電話番号１",
"phone2" => "電話番号２",
"pass1" => "パスワード",
"pass2" => "パスワード確認用",
"mailmagazine" => "メールマガジンの可否",
"ninki" => "好きな人"

);


if($_POST["register"] == "1"){






foreach($list_r as $key => $val){
${$key} = $_POST[$key];
/*if(${$key} == ""){
echo $error[$key] = $val."が入力されていません<br />";
$error_checker = 1;
}*/
}

if(substr($pass1,5,1) == "" ){
$error["pass1"] = "<font color='red'>パスワードは６文字以上です。</font><br />";
}
if($pass1 != $pass2){
$error["pass2"] = "<font color='red'>パスワード確認用がマッチしていません。</font><br />";
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
   $subject = "Jacksファンクラブ登録完了"; 
   $message = "JacKsオフィシャルファンクラブ事務局でございます。

お手続きありがとうございます。
ファンクラブ会員仮登録が完了致しました。

お手数ですが、下記の金額を指定の振込先まで
ご入金の程よろしくお願い致します。


[ ファンクラブ会員 年会費 ]

年会費：￥3,000

↓↓↓↓↓↓↓↓↓↓

2012/6/7までのご入金なら
年会費：￥2,500




[ 振込先 ]

あすか信用組合 本店営業部 普通 0167183  
(株)ドア・マウンド




JacKsオフィシャルファンクラブ事務局


";
   
   mb_send_mail($to, $subject, $message, $header); 


 $to = "queens@triple-kmen.com";
   $header = "From: $from\n";  
   $header .= "Reply-To: $reply_to\n";
   $header .= "X-Mailer: myphpMail ". phpversion(). "\n"; 
   $subject = "Jacksファンクラブ登録完了通知"; 
   $message = "下記の登録がありました。

#####登録内容#####
";

foreach($list_r as $key => $val){
	$message .= "■".$val."
".${$key}."

";
}


   
   mb_send_mail($to, $subject, $message, $header); 

}

}

if(!isset($error["pass1"]) && !isset($error["pass2"]) && $_POST["register"] == 1){

?>



		<h2 class="sh_heading_main_b"><span>ファンクラブ会員登録が完了しました。</span></h2>
<p><br />
				  <br />
				  <br />
				  ご登録、ありがとうございます。<br />
				  JacKsオフィシャルファンクラブへの登録が完了いたしました。<br />
				  <br />
				</p>
				<ul>
				  事務局からの「JacKsファンクラブ会員登録完了メール」をご確認の上、<br />
				  JacKs事務局指定の口座までご入金ください。
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
	    <td><span class="registitem">※お名前(全角)</span></td>
	    <td colspan="2"><span class="back">姓</span>
	      <input name="sei" type="text" required="required" value="<?php echo $sei; ?>" size="15" maxlength="20" />
	      <span class="both">　名</span>
	      <input name="mei" type="text" required="required" value="<?php echo $mei; ?>" size="15" maxlength="20" /></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※フリガナ(全角)</span></td>
	    <td colspan="2"><span class="back">セイ</span>
	      <input name="sei2" type="text" required="required" value="<?php echo $sei2; ?>" size="15" maxlength="20" />
	      　
				<span class="both">メイ</span>
				<input name="mei2" type="text" required="required" value="<?php echo $mei2; ?>" size="15" maxlength="20" /></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">※ニックネーム(全角半角可)</span></td>
	    <td colspan="2"><input type="text" name="nickname" required="required" value="<?php echo $nickname; ?>" class="wtype4" id="nickname" onblur="checkNickName()" /></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">※メールアドレス1 (PC or 携帯)</span></td>
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
	    <td><span class="registitem">メールアドレス2 (PC or 携帯)</span></td>
	    <td colspan="2"><input type="text" name="email2" value="<?php echo $email2; ?>" class="wtype5" /></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※性別</span></td>
	    <td><input type="radio" name="gender" value="男性" <?php if($gender == 2){ echo ' checked="checked" ';}?> />
	      <span class="back">男性</span>
          <input type="radio" name="gender" value="女性" <?php if($gender != 2){ echo ' checked="checked" ';}?> />
          女性</td>
	    <td>&nbsp;</td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※生年月日</span></td>
	    <td colspan="2"><input name="birth_year" type="text" required="required" class="wtype2" value="<?php echo $birth_year; ?>" size="10" maxlength="4" />
          <span class="back">年</span>
          <input name="birth_month" type="text" required="required" class="wtype1" value="<?php echo $birth_month; ?>" size="4" maxlength="2" />
          <span class="back">月</span>
          <input name="birth_day" type="text" required="required" class="wtype1" value="<?php echo $birth_day; ?>" size="4" maxlength="2" />
          <span>日</span></td>
	    </tr>
	  <tr>
	    <td valign="top"><span class="registitem">※住所</span></td>
	    <td colspan="2" nowrap="nowrap" class="back">郵便番号
	      <input name="czip" type="text" required="required" id="czip" value="<?php echo $czip; ?>" size="5" maxlength="3" />
	      -
	      <input name="czip2" type="text" required="required" id="czip2" value="<?php echo $czip2; ?>" size="5" maxlength="4" />
	      <br />
都道府県
<input type="text" name="pref" required="required" value="<?php echo $pref; ?>" id="pref2" />
<br />
<span class="registitem"></span>市区町村
<input type="text" name="addr" required="required" value="<?php echo $addr; ?>" class="wtype4" id="addr2" />
<span class="front">(例)新宿区大久保</span><br />
<span class="registitem"></span>番地/建物名(全角)
<input type="text" name="addr2" required="required" value="<?php echo $addr2; ?>" class="wtype5" />
<span class="front">(例)1-12-4 ASS第2ビル5F</span></td>
	    </tr>
	  <tr>
	    <td nowrap="nowrap"><span class="registitem">※連絡先電話番号1(自宅 or 携帯)</span></td>
	    <td colspan="2"><input type="text" name="phone1" required="required" value="<?php echo $phone1; ?>" class="wtype4" />	      <span class="front">(注)半角数字、ハイフンなし</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">連絡先電話番号2(自宅 or 携帯)</span></td>
	    <td colspan="2"><input type="text" name="phone2" value="<?php echo $phone2; ?>" class="wtype4" />	      <span class="front">(注)半角数字、ハイフンなし</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※パスワード</span></td>
	    <td colspan="2"><?php if(isset($error["pass1"])){echo $error["pass1"]; } ?><input type="password" name="pass1" required="required" value="" />	      <span class="front">※6桁以上の半角英数字</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※パスワード確認用</span></td>
	    <td colspan="2"><?php if(isset($error["pass2"])){echo $error["pass2"]; } ?><input type="password" name="pass2" required="required" value="" />	      <span class="front">※6桁以上の半角英数字</span></td>
	    </tr>


	  <tr>
	    <td><span class="registitem">※JacKsで一番好きな人は誰ですか？</span></td>
	        <td colspan="2"><input type="radio" name="ninki" value="イ・シヒョン" <?php if($ninki == "イ・シヒョン"){ echo ' checked="checked" ';}?> />
	      <span class="back">イ・シヒョン</span>
	      <input type="radio" name="ninki" value="ミッキー" <?php if($ninki == "ミッキー"){ echo ' checked="checked" ';}?>/>
	      <span class="back">ミッキー</span>
          <input type="radio" name="ninki" value="ナ・クン"  <?php if($ninki == "ナ・クン"){ echo ' checked="checked" ';}?>/>
	      <span class="back">ナ・クン</span></td>
	    </tr>
	  <tr>
	    <td><span class="registitem">※メールマガジン</span></td>
	    <td colspan="2"><input type="radio" name="mailmagazine" value="受信する" <?php if($mailmagazine == 1){ echo ' checked="checked" ';}?> />
	      <span class="back">受信する　</span>
	      <input type="radio" name="mailmagazine" value="受信しない" <?php if($mailmagazine != 1){ echo ' checked="checked" ';}?>/>
	      受信しない</td>
	    </tr>
	  </table>
	<br />
	<br />
   <fieldset>
     <p>
<input type="hidden" name="register" value="1">
       <input type="submit" value="送信する">
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
        	<p class="sh_menu_list"><a href="index.php" title="会員登録トップ">会員登録トップ</a></p>
			<p class="sh_menu_list"><a href="index.php#tokuten" title="会員特典">会員特典</a></p>
			<p class="sh_menu_list"><a href="index.php#kiyaku" title="利用規約">利用規約</a></p>
			<p class="sh_menu_list"><a href="http://triple-kmen.com/" title="トリプルKトップ">トリプルKトップ</a></p>
		</div>
	</div><!-- /menu -->
<div><img src="image/footer.gif" width="900" height="170" align="right"></div>
</div><!-- /container -->

<!-- /display:noneタグ -->
</body>
</html>
