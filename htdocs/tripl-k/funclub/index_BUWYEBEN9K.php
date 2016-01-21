<?php

if($mail = $_POST['email'])

if (preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $mail)) {


   mb_language('ja');
   mb_internal_encoding("Shift-JIS");
 
   $from = 'queens@triple-kmen.com'; 
   $reply_to = 'queens@triple-kmen.com'; 
   $to = $mail;
   $header = "From: $from\n";  
   $header .= "Reply-To: $reply_to\n";
   $header .= "X-Mailer: myphpMail ". phpversion(). "\n"; 
   $subject = "Jacksファンクラブ登録"; 
   $message = "JacKsオフィシャルファンクラブ事務局でございます。

下記URLより、お客様情報入力ページにお進みいただき、ファンクラブ会員登録を行なってください。

http://triple-kmen.com/funclub/touroku.php?jid=".urlencode($mail)."

※当メールに身に覚えのない場合は、お手数ですが破棄くださいますようお願いいたします。
※URLをクリックしても移動できない場合は、お手数ですが、メールに記載されているURLをブラウザのアドレス欄に
直接コピー＆ペーストしてエンターキーを押してください。

JacKsオフィシャルファンクラブ事務局
";
   
   mb_send_mail($to, $subject, $message, $header); 
	$checker = 1;
} else {
	$error = "<font color='red'>フォーマットが不正です。</font><br />";
}

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-Transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
<title>Jacksオフィシャルファンクラブ 会員登録</title>
<meta name="description" content="JacKs[ジャックス]オフィシャルファンクラブに入会希望の方はこちらから" />
<meta name="keywords" content="新大久保 トリプルK,Jacks オフィシャルファンクラブ 会員登録,ジャックス" />
<meta name="robots" content="noindex, nofollow, noarchive">
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />

<link rel="stylesheet" type="text/css" href="./css/common.css" />
<link rel="stylesheet" type="text/css" href="./css/share.css" />
<link rel="stylesheet" type="text/css" href="./css/jp/common_side.css" />

<link rel="stylesheet" type="text/css" href="css/slicebox.css" />
<script type="text/javascript" src="js/modernizr.custom.13303.js"></script>
<script src="Scripts/swfobject_modified.js" type="text/javascript"></script>
</head>
<body>
<!-- header_box -->

<!-- /header_box -->

<div id="container" class="clear">


<?php
   $Agent = getenv( "HTTP_USER_AGENT" );
    /* 環境変数 HTTP_USER_AGENT を見て、正規表現のマッチングをする(ereg)。*/
   if( ereg( "MSIE", $Agent ) ){ ?>

<div class="container">  

<object id="FlashID" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="990" height="700">
  <param name="movie" value="images/fla.swf" />
  <param name="quality" value="high" />
  <param name="wmode" value="opaque" />
  <param name="swfversion" value="11.0.0.0" />
  <!-- このパラメータータグにより、Flash Player 6.0 または 6.5 以降を使用して、Flash Player の最新バージョンをダウンロードするようメッセージが表示されます。ユーザーにメッセージを表示させないようにする場合はパラメータータグを削除します。 -->
  <param name="expressinstall" value="Scripts/expressInstall.swf" />
  <!-- 次のオブジェクトタグは IE 以外のブラウザーで使用するためのものです。IE では IECC を使用して非表示にします。 -->
  <!--[if !IE]>-->
  <object type="application/x-shockwave-flash" data="images/fla.swf" width="990" height="700">
    <!--<![endif]-->
    <param name="quality" value="high" />
    <param name="wmode" value="opaque" />
    <param name="swfversion" value="11.0.0.0" />
    <param name="expressinstall" value="Scripts/expressInstall.swf" />
    <!-- ブラウザーには、Flash Player 6.0 以前のバージョンを使用して次の代替コンテンツが表示されます。 -->
    <div>
      <h4>このページのコンテンツには、Adobe Flash Player の最新バージョンが必要です。</h4>
      <p><a href="http://www.adobe.com/go/getflashplayer"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Adobe Flash Player を取得" width="112" height="33" /></a></p>
    </div>
    <!--[if !IE]>-->
  </object>
  <!--<![endif]-->
</object>
</div> 

<?php }else{ ?>

<div id="header">
   		  <div class="container">           
			<div id="sb-slider" class="sb-slider">
				<img src="images/1.jpg" title="JacKs Official FanClub"/>
				<img src="images/2.jpg" title="イ・シヒョン　プロフィール"/>
				<img src="images/3.jpg" title="ミッキー　プロフィール"/>
				<img src="images/4.jpg" title="ナクン　プロフィール"/>
			</div>        
	</div>
        
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
		<script type="text/javascript" src="js/jquery.slicebox.min.js"></script>
		<script type="text/javascript">
			$(function() {

				$('#sb-slider').slicebox({
					slideshow		: true,
					slideshowTime		:3000
				});
				
				if( !Modernizr.csstransforms3d ) {
					$('#sb-note').show();
					
					$('body').append(
						$('script').attr( 'type', 'text/javascript' ).attr( 'src', 'js/jquery.easing.1.3.js' )
					);
				}	
			});
		</script>
        
  </div>
<?php } ?>

<?php if($checker != 1){ ?>
	<div id="main" class="clear">
		<div id="content" class="clear">
			<p><strong></strong></p>
            <iframe width="680" height="383" src="http://www.youtube.com/embed/N3OxowW_HRg?autoplay=1&loop=1&rel=0" frameborder="0" allowfullscreen></iframe>
            <p><strong></strong></p>
            <br />
            <p>JacKsオフィシャルファンクラブに入会希望の方は、注意事項、<a href="#kiyaku" target="_blank" style="text-decoration:underline;">利用規約</a>をお読みになり、ご同意の上、メールアドレスを入力してください。<br />
<br />
		  <form name="form_input_email" method="post" action="index.php" onSubmit="return email_form_check()">
				<h2 class="sh_heading_main_b"><span>メールアドレスの入力</span></h2>
				<p>仮登録のメールを送信します。受信可能なメールアドレスを入力してください。<br />
			    到着したメールに記載してあるURLをクリックすると、本登録の画面へ進みます。</p>
				<br />
				<table id="no-login-table">
				<tr>
				  <td><?php echo $error; ?>あなたのメールアドレス(PC or 携帯): 
				    <input type="text" id="email" name="email" required>　<input type="submit" value="規約に同意して送信"></td></tr>
				</table>
				<br /><br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">登録時の注意事項</h3>
				<ul>
				  ● 既に登録済みのメールアドレスはご登録いただけません。<br />
<p style="color:red;">● 携帯メールアドレスをご入力いただくお客様でドメイン指定受信設定をされている場合「triple-kmen.com」を受信ドメインに追加してください。</p>
				  <li>● 携帯メールアドレスをご入力いただくお客様で、メールアドレスの文字列中に連続する...(ドット)が入っている、もしくは「- (ハイフン)」から始まるメールアドレスの場合は、システムの仕様上折り返しのメールが届きませんので、メールアドレスの変更及び別のメールアドレスでのご登録をお願いいたします。</li>
				  <li>● 携帯メールアドレスをご入力されたお客様は、届いたメールをPCメールに転送してから、URLのクリックをお願いいたします。</li>
				  <li>● メールアドレスはすべて半角英数字でご入力ください。</li>
				  <li>● 3日を経過しても仮登録の登録手続きが完了していない場合は、再度メール認証からの登録になります。</li>
				  <li>・Yahoo!メールやGmailなどのフリーメールアドレスをご利用の場合、迷惑メールフォルダに送信されることが御座います。</li>
            </ul>
				<p>&nbsp;</p>
			  <p id="enter">&nbsp;</p>
              


			<h2 class="sh_heading_main_b" id="tokuten"><span>会員特典</span></h2>
				<br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">入会金／年会費</h3>
				<ul>
				  JacKsオフィシャルファンクラブ<br />
			      年会費：￥3,000
				  &rarr; 2012/6/7までのお申込みなら ￥2,500<br />
				  ファンクラブへの入会をご希望の際は、事務局からの「JacKsファンクラブ会員登録完了メール」をご確認の上、JacKs事務局指定の口座までご入金ください。<br />
				  <br />
<p style="font-weight:bold">振込先：あすか信用組合 本店営業部 普通 0167183  (株)ドア・マウンド<br /></p>
【※恐れ入りますが振込み手数料はご負担下さい】
<br /><br /><br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">料金割引</h3>
				 チケット料金を会員価格でご提供致します！！
一般価格￥2,000 ⇒ 会員価格￥1,800<br />
バータイム2,000円&rarr;1,000円<br />
※未成年者については他に特典あり。<br />
<br />
<br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">会員証</h3>
                  <p>JacKsファンクラブにご入会いただきますと、会員証を発行致します。
                    会員証にはファンクラブの証となる、あなただけの会員番号が刻印されているカードです。<br />
                  </p>
				  <br />
				  <br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">その他</h3>
こちらの会員特典は2012年6月現在の特典です。変更になる場合もありますので、予めご理解頂きますようお願い致します。<br />
			</ul>
<p id="enter">&nbsp;</p>

              
			<h2 class="sh_heading_main_b" id="kiyaku"><span>利用規約</span></h2>
				<br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">第1条（基本規約）</h3>
				<ul>
				  <li>				  申し込みをした会員（以下、「申込者」といいます。）は、このチケット規約（以下｢本規約｣といいます。）を承諾したものとみなします。<br />
				    <br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">第2条（チケットの販売）</h3>
				  1　チケットの販売は、当社が適当と判断した方法により行います。<br />
				  2　公演のチケットについては先着順とし、その他当社が取り扱うチケットは申込者が多数の場合、整理券については、抽選により入場順を決め、当社が適当と判断した公平かつ公正な方法により抽選を行うものとします。<br /><br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">第3条（申し込みの無効）</h3>
				  当社は、次の各号のいずれかに該当する事実がある場合、申し込みを無効とし、または前条第2項の抽選による当選を取り消すことができるものとします。<br />
				  1　同一住所で多数の申し込みがあった場合（家族、同居者は除く。）<br />
				  2　同一筆跡で名義の異なる多数の申し込みがあった場合<br />
				  3　申込者の住所地が法人の営業所である場合<br />
				  4　申込者が実在しない場合、あるいは実在が疑われる場合<br />
				  5　申込者が第三者への転売目的その他申込者以外の第三者に利用させる目的で申し込みを行った場合、またはかかる目的で申し込みを行ったものと当社が判断した場合<br />
				  6　申込者が、申込をした時点で本規約の違反等により資格の停止処分中であった場合<br />
				  7　申込書の記載事項に、虚偽記載、誤記、または記入漏れがあった場合<br />
				  <br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">第４条（入場制限等)</h3>
1　当社は、次の各号に該当する場合、当該来場者およびその同行者の店内（以下｢会場｣といいます。）への入場を制限し、または退場を求めることがあります。なお、この場合、チケットの代金は返還しないものとします。<br />
・チケットが申込者本人のものであるかどうかを確認するためにファンクラブの会員番号および身分証明書の提示を求められた場合に、これを理由なく拒否した場合<br />
・来場者が申込者本人であると確認できない場合<br />
・正規の販売代金以上の金額で購入したチケットを所持している場合<br />
・会場にカメラ、ビデオ等の録音、録画、撮影機器を持ち込んだ場合または持ち込もうした場合<br />
・会場において撮影、録画または録音行為を行った場合（携帯電話による撮影も含む）<br />
・会場において、主催者の指示に従わなかった場合<br />
・会場において、違法に撮影された写真またはビデオ等を購入した場合<br />
・出演者等に対し、過剰な付きまとい行為または誹謗中傷行為を行った場合<br />
・会場において、他の入場者に迷惑をかける行為を行った場合<br />
2　申込者は、前項各号の行為により他の来場者、コンサートスタッフ、アーティストその他の第三者に対し損害を与えた場合、これを賠償する責任を負います。<br />
3　当社は、第１項各号の行為を行った者に対しては、当社の判断により、以後一切のチケットの販売を行わないものとする場合があります。<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">第５条（申込者の個人情報の開示）</h3>
当社は、裁判所や警察署の公的機関から、法律に基づく正式な照会を受けた場合、申込者の個人情報を開示することがあります。<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">第６条（規約の変更）</h3>
当社は、申込者に対し何らの通知を行うことなく、本規約の内容を変更、追加、修正、削除することができるものとします。<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">第７条（協議事項）</h3>
本規約に定めのない事項または本規約の解釈について疑義が生じた場合、申込者および当社は双方誠意を持って協議の上これを解決するものとします。</li>
            </ul>
				<p>&nbsp;</p>
                <div class="footerimg"><img src="image/t1-sita.jpg" align="right"></div>
		    <p id="enter">&nbsp;</p>
		  </form>
          <div><img src="image/footer.gif" width="900" height="170" align="right"></div>
		</div>
	</div><!-- /main -->
<?php }else{ ?>
	<div id="main" class="clear">
		<div id="content" class="clear">

		<h2 class="sh_heading_main_b"><span>メールアドレスの送信完了</span></h2>
        <br /><br /><br /><br />
<p>登録いただいたアドレス宛に会員登録フォームのURLを記載したメールを送信しました。<br />メールに記載されたURLをクリックして、会員登録フォームにお進みください。</p>

</div>
<br /><br /><br /><br /><br /><br /><br /><br />
</div>
<div><img src="image/footer.gif" width="900" height="170" align="right"></div>

<?php } ?>

		<div id="menu">
		<div class="sh_menu">
        <p class="sh_menu_list"><a href="index.php" title="会員登録トップ">会員登録トップ</a></p>
			<p class="sh_menu_list"><a href="#tokuten" title="会員特典">会員特典</a></p>
			<p class="sh_menu_list"><a href="#kiyaku" title="利用規約">利用規約</a></p>
			<p class="sh_menu_list"><a href="http://triple-kmen.com/" title="トリプルKトップ">トリプルKトップ</a></p>
		</div>
        <div class="sh_banner"><br />
        <a href="http://ameblo.jp/queens20120601/"><img src="image/queens_oficial_blog.jpg" width="200"></a></div>
	    <div class="sh_banner"><br />
        <a href="http://ameblo.jp/jacks0118"><img src="image/jacks_oficial_blog.jpg" width="200"></a></div>
	
    </div><!-- /menu -->

</div><!-- /container -->

<div style="display:none;">

</div><!-- /display:noneタグ -->
<script type="text/javascript">
swfobject.registerObject("FlashID");
</script>
</body>
</html>
<?php
echo "<mm:dwdrfml documentRoot=＼"" . __FILE__ .	"＼" >＼n＼n";
$included_files = get_included_files();
foreach ($included_files as $filename) {
	echo "<mm:IncludeFile path=＼"$filename＼" />＼n＼n";
}
echo "</mm:dwdrfml>＼n＼n";

?>