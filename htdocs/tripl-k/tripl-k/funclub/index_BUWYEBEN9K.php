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
   $subject = "Jacks�t�@���N���u�o�^"; 
   $message = "JacKs�I�t�B�V�����t�@���N���u�����ǂł������܂��B

���LURL���A���q�l�����̓y�[�W�ɂ��i�݂��������A�t�@���N���u����o�^���s�Ȃ��Ă��������B

http://triple-kmen.com/funclub/touroku.php?jid=".urlencode($mail)."

�������[���ɐg�Ɋo���̂Ȃ��ꍇ�́A���萔�ł����j�����������܂��悤���肢�������܂��B
��URL���N���b�N���Ă��ړ��ł��Ȃ��ꍇ�́A���萔�ł����A���[���ɋL�ڂ���Ă���URL���u���E�U�̃A�h���X����
���ڃR�s�[���y�[�X�g���ăG���^�[�L�[�������Ă��������B

JacKs�I�t�B�V�����t�@���N���u������
";
   
   mb_send_mail($to, $subject, $message, $header); 
	$checker = 1;
} else {
	$error = "<font color='red'>�t�H�[�}�b�g���s���ł��B</font><br />";
}

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-Transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
<title>Jacks�I�t�B�V�����t�@���N���u ����o�^</title>
<meta name="description" content="JacKs[�W���b�N�X]�I�t�B�V�����t�@���N���u�ɓ����]�̕��͂����炩��" />
<meta name="keywords" content="�V��v�� �g���v��K,Jacks �I�t�B�V�����t�@���N���u ����o�^,�W���b�N�X" />
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
    /* ���ϐ� HTTP_USER_AGENT �����āA���K�\���̃}�b�`���O������(ereg)�B*/
   if( ereg( "MSIE", $Agent ) ){ ?>

<div class="container">  

<object id="FlashID" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="990" height="700">
  <param name="movie" value="images/fla.swf" />
  <param name="quality" value="high" />
  <param name="wmode" value="opaque" />
  <param name="swfversion" value="11.0.0.0" />
  <!-- ���̃p�����[�^�[�^�O�ɂ��AFlash Player 6.0 �܂��� 6.5 �ȍ~���g�p���āAFlash Player �̍ŐV�o�[�W�������_�E�����[�h����悤���b�Z�[�W���\������܂��B���[�U�[�Ƀ��b�Z�[�W��\�������Ȃ��悤�ɂ���ꍇ�̓p�����[�^�[�^�O���폜���܂��B -->
  <param name="expressinstall" value="Scripts/expressInstall.swf" />
  <!-- ���̃I�u�W�F�N�g�^�O�� IE �ȊO�̃u���E�U�[�Ŏg�p���邽�߂̂��̂ł��BIE �ł� IECC ���g�p���Ĕ�\���ɂ��܂��B -->
  <!--[if !IE]>-->
  <object type="application/x-shockwave-flash" data="images/fla.swf" width="990" height="700">
    <!--<![endif]-->
    <param name="quality" value="high" />
    <param name="wmode" value="opaque" />
    <param name="swfversion" value="11.0.0.0" />
    <param name="expressinstall" value="Scripts/expressInstall.swf" />
    <!-- �u���E�U�[�ɂ́AFlash Player 6.0 �ȑO�̃o�[�W�������g�p���Ď��̑�փR���e���c���\������܂��B -->
    <div>
      <h4>���̃y�[�W�̃R���e���c�ɂ́AAdobe Flash Player �̍ŐV�o�[�W�������K�v�ł��B</h4>
      <p><a href="http://www.adobe.com/go/getflashplayer"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Adobe Flash Player ���擾" width="112" height="33" /></a></p>
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
				<img src="images/2.jpg" title="�C�E�V�q�����@�v���t�B�[��"/>
				<img src="images/3.jpg" title="�~�b�L�[�@�v���t�B�[��"/>
				<img src="images/4.jpg" title="�i�N���@�v���t�B�[��"/>
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
            <p>JacKs�I�t�B�V�����t�@���N���u�ɓ����]�̕��́A���ӎ����A<a href="#kiyaku" target="_blank" style="text-decoration:underline;">���p�K��</a>�����ǂ݂ɂȂ�A�����ӂ̏�A���[���A�h���X����͂��Ă��������B<br />
<br />
		  <form name="form_input_email" method="post" action="index.php" onSubmit="return email_form_check()">
				<h2 class="sh_heading_main_b"><span>���[���A�h���X�̓���</span></h2>
				<p>���o�^�̃��[���𑗐M���܂��B��M�\�ȃ��[���A�h���X����͂��Ă��������B<br />
			    �����������[���ɋL�ڂ��Ă���URL���N���b�N����ƁA�{�o�^�̉�ʂ֐i�݂܂��B</p>
				<br />
				<table id="no-login-table">
				<tr>
				  <td><?php echo $error; ?>���Ȃ��̃��[���A�h���X(PC or �g��): 
				    <input type="text" id="email" name="email" required>�@<input type="submit" value="�K��ɓ��ӂ��đ��M"></td></tr>
				</table>
				<br /><br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">�o�^���̒��ӎ���</h3>
				<ul>
				  �� ���ɓo�^�ς݂̃��[���A�h���X�͂��o�^���������܂���B<br />
<p style="color:red;">�� �g�у��[���A�h���X�������͂����������q�l�Ńh���C���w���M�ݒ������Ă���ꍇ�utriple-kmen.com�v����M�h���C���ɒǉ����Ă��������B</p>
				  <li>�� �g�у��[���A�h���X�������͂����������q�l�ŁA���[���A�h���X�̕����񒆂ɘA������...(�h�b�g)�������Ă���A�������́u- (�n�C�t��)�v����n�܂郁�[���A�h���X�̏ꍇ�́A�V�X�e���̎d�l��܂�Ԃ��̃��[�����͂��܂���̂ŁA���[���A�h���X�̕ύX�y�ѕʂ̃��[���A�h���X�ł̂��o�^�����肢�������܂��B</li>
				  <li>�� �g�у��[���A�h���X�������͂��ꂽ���q�l�́A�͂������[����PC���[���ɓ]�����Ă���AURL�̃N���b�N�����肢�������܂��B</li>
				  <li>�� ���[���A�h���X�͂��ׂĔ��p�p�����ł����͂��������B</li>
				  <li>�� 3�����o�߂��Ă����o�^�̓o�^�葱�����������Ă��Ȃ��ꍇ�́A�ēx���[���F�؂���̓o�^�ɂȂ�܂��B</li>
				  <li>�EYahoo!���[����Gmail�Ȃǂ̃t���[���[���A�h���X�������p�̏ꍇ�A���f���[���t�H���_�ɑ��M����邱�Ƃ�������܂��B</li>
            </ul>
				<p>&nbsp;</p>
			  <p id="enter">&nbsp;</p>
              


			<h2 class="sh_heading_main_b" id="tokuten"><span>������T</span></h2>
				<br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">������^�N���</h3>
				<ul>
				  JacKs�I�t�B�V�����t�@���N���u<br />
			      �N���F��3,000
				  &rarr; 2012/6/7�܂ł̂��\���݂Ȃ� ��2,500<br />
				  �t�@���N���u�ւ̓��������]�̍ۂ́A�����ǂ���́uJacKs�t�@���N���u����o�^�������[���v�����m�F�̏�AJacKs�����ǎw��̌����܂ł��������������B<br />
				  <br />
<p style="font-weight:bold">�U����F�������M�p�g�� �{�X�c�ƕ� ���� 0167183  (��)�h�A�E�}�E���h<br /></p>
�y���������܂����U���ݎ萔���͂����S�������z
<br /><br /><br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">��������</h3>
				 �`�P�b�g������������i�ł��񋟒v���܂��I�I
��ʉ��i��2,000 �� ������i��1,800<br />
�o�[�^�C��2,000�~&rarr;1,000�~<br />
�������N�҂ɂ��Ă͑��ɓ��T����B<br />
<br />
<br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">�����</h3>
                  <p>JacKs�t�@���N���u�ɂ�����������܂��ƁA����؂𔭍s�v���܂��B
                    ����؂ɂ̓t�@���N���u�̏؂ƂȂ�A���Ȃ������̉���ԍ������󂳂�Ă���J�[�h�ł��B<br />
                  </p>
				  <br />
				  <br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">���̑�</h3>
������̉�����T��2012�N6�����݂̓��T�ł��B�ύX�ɂȂ�ꍇ������܂��̂ŁA�\�߂����𒸂��܂��悤���肢�v���܂��B<br />
			</ul>
<p id="enter">&nbsp;</p>

              
			<h2 class="sh_heading_main_b" id="kiyaku"><span>���p�K��</span></h2>
				<br />
			<h3 class="sh_heading_sub_main_b" style="height:1.5em;">��1���i��{�K��j</h3>
				<ul>
				  <li>				  �\�����݂���������i�ȉ��A�u�\���ҁv�Ƃ����܂��B�j�́A���̃`�P�b�g�K��i�ȉ���{�K��Ƃ����܂��B�j�������������̂Ƃ݂Ȃ��܂��B<br />
				    <br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">��2���i�`�P�b�g�̔̔��j</h3>
				  1�@�`�P�b�g�̔̔��́A���Ђ��K���Ɣ��f�������@�ɂ��s���܂��B<br />
				  2�@�����̃`�P�b�g�ɂ��Ă͐撅���Ƃ��A���̑����Ђ���舵���`�P�b�g�͐\���҂������̏ꍇ�A�������ɂ��ẮA���I�ɂ����ꏇ�����߁A���Ђ��K���Ɣ��f���������������ȕ��@�ɂ�蒊�I���s�����̂Ƃ��܂��B<br /><br />
				  <h3 class="sh_heading_sub_main_b" style="height:1.5em;">��3���i�\�����݂̖����j</h3>
				  ���Ђ́A���̊e���̂����ꂩ�ɊY�����鎖��������ꍇ�A�\�����݂𖳌��Ƃ��A�܂��͑O���2���̒��I�ɂ�铖�I�����������Ƃ��ł�����̂Ƃ��܂��B<br />
				  1�@����Z���ő����̐\�����݂��������ꍇ�i�Ƒ��A�����҂͏����B�j<br />
				  2�@����M�ՂŖ��`�̈قȂ鑽���̐\�����݂��������ꍇ<br />
				  3�@�\���҂̏Z���n���@�l�̉c�Ə��ł���ꍇ<br />
				  4�@�\���҂����݂��Ȃ��ꍇ�A���邢�͎��݂��^����ꍇ<br />
				  5�@�\���҂���O�҂ւ̓]���ړI���̑��\���҈ȊO�̑�O�҂ɗ��p������ړI�Ő\�����݂��s�����ꍇ�A�܂��͂�����ړI�Ő\�����݂��s�������̂Ɠ��Ђ����f�����ꍇ<br />
				  6�@�\���҂��A�\�����������_�Ŗ{�K��̈ᔽ���ɂ�莑�i�̒�~�������ł������ꍇ<br />
				  7�@�\�����̋L�ڎ����ɁA���U�L�ځA��L�A�܂��͋L���R�ꂪ�������ꍇ<br />
				  <br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">��S���i���ꐧ����)</h3>
1�@���Ђ́A���̊e���ɊY������ꍇ�A���Y����҂���т��̓��s�҂̓X���i�ȉ����ꣂƂ����܂��B�j�ւ̓���𐧌����A�܂��͑ޏ�����߂邱�Ƃ�����܂��B�Ȃ��A���̏ꍇ�A�`�P�b�g�̑���͕Ԋ҂��Ȃ����̂Ƃ��܂��B<br />
�E�`�P�b�g���\���Җ{�l�̂��̂ł��邩�ǂ������m�F���邽�߂Ƀt�@���N���u�̉���ԍ�����ѐg���ؖ����̒񎦂����߂�ꂽ�ꍇ�ɁA����𗝗R�Ȃ����ۂ����ꍇ<br />
�E����҂��\���Җ{�l�ł���Ɗm�F�ł��Ȃ��ꍇ<br />
�E���K�̔̔�����ȏ�̋��z�ōw�������`�P�b�g���������Ă���ꍇ<br />
�E���ɃJ�����A�r�f�I���̘^���A�^��A�B�e�@����������񂾏ꍇ�܂��͎��������������ꍇ<br />
�E���ɂ����ĎB�e�A�^��܂��͘^���s�ׂ��s�����ꍇ�i�g�ѓd�b�ɂ��B�e���܂ށj<br />
�E���ɂ����āA��Î҂̎w���ɏ]��Ȃ������ꍇ<br />
�E���ɂ����āA��@�ɎB�e���ꂽ�ʐ^�܂��̓r�f�I�����w�������ꍇ<br />
�E�o���ғ��ɑ΂��A�ߏ�ȕt���܂Ƃ��s�ׂ܂��͔�排����s�ׂ��s�����ꍇ<br />
�E���ɂ����āA���̓���҂ɖ��f��������s�ׂ��s�����ꍇ<br />
2�@�\���҂́A�O���e���̍s�ׂɂ�葼�̗���ҁA�R���T�[�g�X�^�b�t�A�A�[�e�B�X�g���̑��̑�O�҂ɑ΂����Q��^�����ꍇ�A����𔅏�����ӔC�𕉂��܂��B<br />
3�@���Ђ́A��P���e���̍s�ׂ��s�����҂ɑ΂��ẮA���Ђ̔��f�ɂ��A�Ȍ��؂̃`�P�b�g�̔̔����s��Ȃ����̂Ƃ���ꍇ������܂��B<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">��T���i�\���҂̌l���̊J���j</h3>
���Ђ́A�ٔ�����x�@���̌��I�@�ւ���A�@���Ɋ�Â������ȏƉ���󂯂��ꍇ�A�\���҂̌l�����J�����邱�Ƃ�����܂��B<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">��U���i�K��̕ύX�j</h3>
���Ђ́A�\���҂ɑ΂�����̒ʒm���s�����ƂȂ��A�{�K��̓��e��ύX�A�ǉ��A�C���A�폜���邱�Ƃ��ł�����̂Ƃ��܂��B<br /><br />
<h3 class="sh_heading_sub_main_b" style="height:1.5em;">��V���i���c�����j</h3>
�{�K��ɒ�߂̂Ȃ������܂��͖{�K��̉��߂ɂ��ċ^�`���������ꍇ�A�\���҂���ѓ��Ђ͑o�����ӂ������ċ��c�̏ケ�������������̂Ƃ��܂��B</li>
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

		<h2 class="sh_heading_main_b"><span>���[���A�h���X�̑��M����</span></h2>
        <br /><br /><br /><br />
<p>�o�^�����������A�h���X���ɉ���o�^�t�H�[����URL���L�ڂ������[���𑗐M���܂����B<br />���[���ɋL�ڂ��ꂽURL���N���b�N���āA����o�^�t�H�[���ɂ��i�݂��������B</p>

</div>
<br /><br /><br /><br /><br /><br /><br /><br />
</div>
<div><img src="image/footer.gif" width="900" height="170" align="right"></div>

<?php } ?>

		<div id="menu">
		<div class="sh_menu">
        <p class="sh_menu_list"><a href="index.php" title="����o�^�g�b�v">����o�^�g�b�v</a></p>
			<p class="sh_menu_list"><a href="#tokuten" title="������T">������T</a></p>
			<p class="sh_menu_list"><a href="#kiyaku" title="���p�K��">���p�K��</a></p>
			<p class="sh_menu_list"><a href="http://triple-kmen.com/" title="�g���v��K�g�b�v">�g���v��K�g�b�v</a></p>
		</div>
        <div class="sh_banner"><br />
        <a href="http://ameblo.jp/queens20120601/"><img src="image/queens_oficial_blog.jpg" width="200"></a></div>
	    <div class="sh_banner"><br />
        <a href="http://ameblo.jp/jacks0118"><img src="image/jacks_oficial_blog.jpg" width="200"></a></div>
	
    </div><!-- /menu -->

</div><!-- /container -->

<div style="display:none;">

</div><!-- /display:none�^�O -->
<script type="text/javascript">
swfobject.registerObject("FlashID");
</script>
</body>
</html>
<?php
echo "<mm:dwdrfml documentRoot=�_"" . __FILE__ .	"�_" >�_n�_n";
$included_files = get_included_files();
foreach ($included_files as $filename) {
	echo "<mm:IncludeFile path=�_"$filename�_" />�_n�_n";
}
echo "</mm:dwdrfml>�_n�_n";

?>