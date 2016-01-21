#!/usr/bin/perl

###############################################
#   diary14.cgi
#      V2.1 (2010.10.2)
#                     Copyright(C) CGI-design
###############################################

require './cgi-lib.pl';

$script = 'diary14.cgi';
$base = './diadata';				#データ格納ディレクトリ
$nofile = "$base/no.txt";			#記事番号
$opfile = "$base/option.txt";
$cgi_lib'maxdata = 300000;			#入力最大容量（byte）

open (IN,"$opfile") || &error("OPEN ERROR");	$opdata = <IN>;		close IN;
if (!$opdata) {
	$pass = &crypt('cgi');
	chmod(0666,$opfile);	open (OUT,">$opfile") || &error("OPEN ERROR");
	print OUT "$pass<>日記<><><><>$base<>$base<>#fafaf5,#000000,#c00000,#764747,#ffffff,#ffffff<>700<>200";
	close OUT;
	chmod(0666,$nofile);
}

### メイン処理 ###
&ReadParse;
while (($n,$val) = each %in) {
	if ($n eq 'img') {next;}
	$val =~ s/&/&amp;/g;	$val =~ s/</&lt;/g;		$val =~ s/>/&gt;/g;		$val =~ s/"/&quot;/g;	$val =~ s/\r\n|\r|\n/<br>/g;
	$in{$n} = $val;
}
$mode = $in{'mode'};
$logyear = $in{'year'};
$logmon = $in{'mon'};
$logday = $in{'day'};

open (IN,"$opfile") || &error("OPEN ERROR");
($pass,$title,$com_adm,$home,$bg_img,$savedir,$loaddir,$colors,$dspw,$max_wh) = split(/<>/,<IN>);
close IN;
($bg_color,$text_color,$title_color,$frame_color,$sub_color,$combg_color) = split(/,/,$colors);
$back_icon = "$loaddir/back.gif";
$next_icon = "$loaddir/next.gif";

($sec,$min,$hour,$nowday,$nowmon,$nowyear,$nowwday) = localtime;
$nowyear += 1900;
$nowmon++;
if (!$logyear) {$logyear = $nowyear; $logmon = $nowmon;}
$logfile = "$base/$logyear$logmon.txt";

if ($mode eq 'admin') {&admin;} else {&main;}

print "</center></body></html>\n";
exit;

###
sub header {
	print "Content-type: text/html\n\n";
	print "<html><head><META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print "<title>$title</title><link rel=\"stylesheet\" type=\"text/css\" href=\"$loaddir/style.css\"></head>\n";
	$head = 1;
}

###
sub main {
	&header;
	print "<body background=\"$bg_img\" bgcolor=\"$bg_color\" text=\"$text_color\"><center>\n";
	print "<table width=98%><tr><td width=80 valign=top>";
	if ($home) {print "<a href=\"$home\">HOME</a>";}
	print "</td><td align=center><font color=\"$title_color\" size=\"+1\"><h2>$title</h2></font></td><td width=80 align=right></td></tr></table>\n";
	print "<table><tr><td>$com_adm</td></tr></table>\n";

	$mon = $logmon - 1;
	if ($mon < 1) {$mon = 12; $year = $logyear - 1;} else {$year = $logyear;}
	print "<table width=$dspw class=\"moon\"><tr><td width=60 align=right><b>$logyear年</b></td>\n";
	print "<td align=center><a href=\"$script?year=$year&mon=$mon\"><img src=\"$back_icon\" border=0></a>　　<font size=\"+2\"><b>$logmon月</b></font>　　";
	$mon = $logmon + 1;
	if (12 < $mon) {$mon = 1; $year = $logyear + 1;} else {$year = $logyear;}
	print "<a href=\"$script?year=$year&mon=$mon\"><img src=\"$next_icon\" border=0></a></td><td width=60></td></tr></table>\n";
	if (!-e $logfile) {return;}
	&dsp;
}

###
sub dsp {
	open (IN,"$logfile") || &error("OPEN ERROR");
	while (<IN>) {
		($no,$day,$week,$sub,$com,$imgt,$imgw,$imgh) = split(/<>/);
		$com =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href="$2" target="_blank">$2<\/a>/g;

		print "<table width=$dspw bgcolor=\"$frame_color\">\n";
		print "<tr class=\"columnTitle\"><td width=24%><font color=\"$sub_color\" size=\"-1\">$logyear年$logmon月$day日($week)</font></td><td><font color=\"$sub_color\"><b>$sub</b></font></td><td align=right>";
		if ($mode eq 'admin') {print "<input type=submit name=$no value=\"修正\">";}
		print "</td></tr><tr><td colspan=3><table width=100% bgcolor=\"$combg_color\" cellspacing=14><tr><td>\n";
		if ($imgt) {print "<a href=\"$loaddir/$no.$imgt\" target=\"_blank\"><img src=\"$loaddir/$no.$imgt\" width=$imgw height=$imgh hspace=5 border=0 align=right></a>";}
		print "$com</td></tr></table></td></tr></table>\n";
		print "<table width=$dspw><tr><td align=right class=\"toTop\"><a href=\"#\">▲最新情報の先頭</a></td></tr></table>\n";
	}
	close IN;
}

###
sub admin {
	&header;
	print "<body><center>\n";
	$inpass = $in{'pass'};
	if ($inpass eq '') {
		print "<table width=97%><tr><td><a href=\"$script\">戻る</a></td></tr></table>\n";
		print "<br><br><br><br><h4>パスワードを入力して下さい</h4>\n";
		print "<form action=\"$script\" method=POST>\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=password size=10 maxlength=8 name=pass>\n";
		print "<input type=submit value=\" 認証 \"></form>\n";
		print "</center></body></html>\n";
		exit;
	}
	$mat = &decrypt($inpass,$pass);
	if (!$mat) {&error("パスワードが違います");}

	print "<table width=100% bgcolor=\"#8c4600\"><tr><td>　<a href=\"$script\"><font color=\"#ffffff\"><b>戻る</b></font></a></td>\n";
	print "<form action=\"$script\" method=POST><td align=right>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=submit value=\"記事編集\">\n";
	print "<input type=submit name=set value=\"基本設定\"></td></form><td width=10></td></tr></table><br><br><h3>新規記事投稿<h3>\n";

	if ($in{'set'}) {&setup;} else {&edtin;}
}

###
sub edtin {
	if ($in{'newwrt'}) {&newwrt;}
	elsif ($in{'edtwrt'}) {&edtwrt;}
	elsif ($in{'delwrt'}) {&delwrt;}

	&in_form;
	print "<hr width=630><p class=\"attention\">修正、削除する場合は「修正」をクリックして下さい。</p>\n";
	$mon = $logmon - 1;
	if ($mon < 1) {$mon = 12; $year = $logyear - 1;} else {$year = $logyear;}
	print "<table width=$dspw><tr><td width=60 align=right><b>$logyear年</b></td>\n";
	print "<form action=\"$script\" method=POST><td align=right>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=year value=\"$year\">\n";
	print "<input type=hidden name=mon value=\"$mon\">\n";
	print "<input type=image src=\"$back_icon\"></td></form>\n";
	print "<td width=70 align=center><font size=\"+1\"><b>$logmon月</b></font></td>\n";
	$mon = $logmon + 1;
	if (12 < $mon) {$mon = 1; $year = $logyear + 1;} else {$year = $logyear;}
	print "<form action=\"$script\" method=POST><td>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=year value=\"$year\">\n";
	print "<input type=hidden name=mon value=\"$mon\">\n";
	print "<input type=image src=\"$next_icon\"></td></form><td width=60></td></tr></table>\n";
	if (!-e $logfile) {return;}

	print "<table cellpadding=0><tr><form action=\"$script\" method=POST><td>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=year value=\"$logyear\">\n";
	print "<input type=hidden name=mon value=\"$logmon\">\n";
	print "<input type=hidden name=edt value=\"1\"></td></tr></table>\n";
	&dsp;
	print "</form>\n";
}

###
sub in_form {
	print "<table bgcolor=\"#e6e4ce\" cellspacing=10><tr><td><table cellspacing=1 cellpadding=0>\n";
	print "<form action=\"$script\" method=POST enctype=\"multipart/form-data\">\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<tr><td>日付&nbsp;</td><td>";
	if ($in{'edt'}) {
		open (IN,"$logfile") || &error("OPEN ERROR");
		while (<IN>) {
			($no,$day,$week,$sub,$com) = split(/<>/);
			if ($in{$no}) {last;}
		}
		close IN;
		print "<input type=hidden name=year value=\"$logyear\">\n";
		print "<input type=hidden name=mon value=\"$logmon\">\n";
		print "<input type=hidden name=no value=\"$no\">\n";
		print "&nbsp;<b>$logyear年$logmon月$day日($week)</b>";
		$com =~ s/<br>/\r/g;
	} else {
		print "<select name=year>\n";
		for (2010 .. $nowyear+1) {
			if ($_ eq $nowyear) {$sel = ' selected';} else {$sel = '';}
			print "<option value=\"$_\"$sel>$_</option>\n";
		}
		print "</select>年 <select name=mon>\n";
		for (1 .. 12) {
			if ($_ eq $nowmon) {$sel = ' selected';} else {$sel = '';}
			print "<option value=\"$_\"$sel>$_</option>\n";
		}
		print "</select>月 <select name=day>\n";
		for (1 .. 31) {
			if ($_ eq $nowday) {$sel = ' selected';} else {$sel = '';}
			print "<option value=\"$_\"$sel>$_</option>\n";
		}
		print "</select>日";
		$sub = $com = '';
	}
	print "</td></tr>\n";
	print "<tr><td>題名</td><td><input type=text size=70 name=sub value=\"$sub\" style=\"ime-mode:active;\"></td></tr>\n";
	print "<tr><td valign=top><br>内容</td><td><textarea cols=82 rows=22 name=com style=\"ime-mode:active;\">$com</textarea></td></tr>\n";
	print "<tr><td>画像</td><td><input type=file size=70 name=img></td></tr>\n";
	print "<tr><td></td><td>";
	if ($in{'edt'}) {
		print "<table width=100%><tr><td><input type=submit name=edtwrt value=\"修正する\"></td>\n";
		print "<td width=40 bgcolor=red><input type=submit name=delwrt value=\"削除\"></td></tr></table>\n";
	} else {
		print "<input type=submit name=newwrt value=\"新規登録\">";
	}
	print "</td></tr></table></td></tr></table></form>\n";
}

###
sub newwrt {
	&get_wday($logyear,$logmon,$logday);
	open (IN,"$nofile") || &error("OPEN ERROR");		$no = <IN>;			close IN;
	$no++;
	open (OUT,">$nofile") || &error("OPEN ERROR");		print OUT $no;		close OUT;
	&img("$savedir/$no",'img');
	$newdata = "$no<>$logday<>$week<>$in{'sub'}<>$in{'com'}<>$type<>$width<>$height<>\n";

	if (-e $logfile) {
		@new = ();
		$flag = 0;
		open (IN,"$logfile") || &error("OPEN ERROR");
		while (<IN>) {
			($no,$day) = split(/<>/);
			if (!$flag && $day <= $logday) {push(@new,$newdata); $flag = 1;}
			push(@new,$_);
		}
		close IN;
		if (!$flag) {push(@new,$newdata);}
		open (OUT,">$logfile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
	} else {
		open (OUT,">$logfile") || &error("OPEN ERROR");		print OUT $newdata;	close OUT;	chmod(0666,$logfile);
	}
}

###
sub get_wday {
	($y,$m,$d) = @_;
	if ($m < 3) {$y--; $m+=12;}
	$wday = ($y+int($y/4)-int($y/100)+int($y/400)+int((13*$m+8)/5)+$d)%7;
	$week = ('日','月','火','水','木','金','土')[$wday];
}

###
sub edtwrt {
	&img("$savedir/$in{'no'}",'img');
	@new = ();
	open (IN,"$logfile") || &error("OPEN ERROR");
	while (<IN>) {
		($no,$day,$week,$sub,$com,$imgt,$imgw,$imgh) = split(/<>/);
		if ($no eq $in{'no'}) {
			if ($type) {$imgt = $type; $imgw = $width; $imgh = $height;}
			push(@new,"$no<>$day<>$week<>$in{'sub'}<>$in{'com'}<>$imgt<>$imgw<>$imgh<>\n");
		} else {push(@new,$_);}
	}
	close IN;
	open (OUT,">$logfile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
}

###
sub delwrt {
	@new = ();
	open (IN,"$logfile") || &error("OPEN ERROR");
	while (<IN>) {
		($no,$day,$week,$sub,$com,$imgt) = split(/<>/);
		if ($no eq $in{'no'}) {if ($imgt) {unlink "$savedir/$no.$imgt";}} else {push(@new,$_);}
	}
	close IN;
	open (OUT,">$logfile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
}

###
sub setup {
	if ($in{'wrt'}) {
		if ($in{'newpass'} ne '') {$pass = &crypt($in{'newpass'});}
		$title = $in{'title'};
		$com_adm = $in{'com_adm'};
		$home = $in{'home'};		$bg_img = $in{'bg_img'};
		$savedir = $in{'savedir'};	$loaddir = $in{'loaddir'};
		$colors = $in{'colors'};	$colors =~ s/\0/,/g;
		$dspw = $in{'dspw'};
		$max_wh = $in{'max_wh'};

		open (OUT,">$opfile") || &error("OPEN ERROR");
		print OUT "$pass<>$title<>$com_adm<>$home<>$bg_img<>$savedir<>$loaddir<>$colors<>$dspw<>$max_wh";
		close OUT;
	}
	print "下記に入力後、「設定する」を押して下さい。<br><br>\n";
	print "<form action=\"$script\" method=POST>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=set value=\"1\">\n";
	print "<input type=submit name=wrt value=\"設定する\"><br><br>\n";

	print "<table bgcolor=\"#dddddd\" cellspacing=10><tr><td><table cellspacing=1 cellpadding=0>\n";
	print "<tr><td><b>タイトル</b></td><td><input type=text size=60 name=title value=\"$title\"></td></tr>\n";
	$com_adm =~ s/<br>/\r/g;
	print "<tr><td valign=top><br><b>コメント</b></td><td><textarea cols=60 rows=6 name=com_adm>$com_adm</textarea></td></tr>\n";
	print "<tr><td><b>ホームURL</b></td><td><input type=text size=60 name=home value=\"$home\"></td></tr>\n";
	print "<tr><td><b>壁紙</b></td><td><input type=text size=60 name=bg_img value=\"$bg_img\"></td></tr>\n";
	print "<tr><td><b>画像格納ディレクトリ</b></td><td><input type=text size=60 name=savedir value=\"$savedir\"></td></tr>\n";
	print "<tr><td><b>画像読出ディレクトリ</b></td><td><input type=text size=60 name=loaddir value=\"$loaddir\"></td></tr>\n";

	print "<tr><td></td><td><a href=\"$loaddir/color.htm\" target=\"_blank\">カラーコード</a></td></tr>\n";
	@name = ('基本背景色','基本文字色','タイトル色','枠色','見出し色','内容背景色');
	@colors = split(/,/,$colors);
	for (0 .. $#name) {
		print "<tr><td><b>$name[$_]</b></td><td><table cellspacing=0 cellpadding=0><tr>\n";
		print "<td><input type=text size=10 name=colors value=\"$colors[$_]\" style=\"ime-mode:inactive;\"></td>\n";
		print "<td width=5></td><td width=80 bgcolor=\"$colors[$_]\"></td></tr></table></td></tr>\n";
	}
	print "<tr><td><b>記事表\示幅</b></td><td><input type=text size=4 name=dspw value=\"$dspw\" style=\"text-align:right; ime-mode:disabled;\">px</td></tr>\n";
	print "<tr><td><b>画像表\示</b></td><td><input type=text size=4 name=max_wh value=\"$max_wh\" style=\"text-align:right; ime-mode:disabled;\">px</td></tr>\n";
	print "<tr><td><b>パスワード変更</b></td><td><input type=password size=10 maxlength=8 name=newpass> （英数8文字以内）</td></tr>\n";
	print "</table></td></tr></table></form>\n";
}

###
sub img {
	$type=$width=$height=$big=$mac='';
	$imgdata = $in{"$_[1]"};
	if (!$imgdata) {return;}

	foreach (@in) {
		if (/$_[1]/ and /Content-Type:(.+)/i) {
			if ($1 =~ /image\/.*jpeg/i) {$type = 'jpg';}
			elsif ($1 =~ /image\/gif/i) {$type = 'gif';}
			elsif ($1 =~ /image\/.*png/i) {$type = 'png';}
		}
		if (/application\/x-macbinary/i) {$mac = 1;}
	}
	if (!$type) {&error("このファイルはアップロードできません");}

	if ($mac) {
		$leng = substr($imgdata,83,4);
		$leng = unpack("%N",$leng);
		$imgdata = substr($imgdata,128,$leng);
	}
	$img_file = "$_[0].$type";
	open (IMG,">$img_file") || &error("$img_fileファイルを作成できません");
	binmode IMG;
	print IMG $imgdata;
	close IMG;
	chmod (0666,$img_file);

	($t,$width,$height) = &getImageSize("$img_file");
	if (!$width || !$height) {&error("ファイルを認識できません");}

	if ($max_wh && ($max_wh < $width || $max_wh < $height)) {
		if ($height < $width) {$height = int($height * $max_wh / $width); $width = $max_wh;}
		else {$width = int($width * $max_wh / $height); $height = $max_wh;}
		$big = 1;
	}
}

#=========================================
# Get Image Pixel Size.（出典：stdio-902）
#=========================================
sub getImageSize {
	local($file_name) = @_;
	local($head);

	return if (!open IMG, $file_name);
	binmode IMG;
	read IMG, $head, 8;
	if ($head eq "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a") {
		local($width, $height);
		if (read(IMG, $head, 4) != 4 || read(IMG, $head, 4) != 4 || $head ne 'IHDR') {
			close IMG;
			return "PNG", 0;
		}
		read IMG, $head, 8;
		close IMG;
		$width = unpack "N", substr($head, 0, 4);
		$height = unpack "N", substr($head, 4, 4);
		return "PNG", $width, $height;
	}
	$head = substr $head, 0, 3;
	if ($head eq "\x47\x49\x46") {
		local($head, $width, $height);
		seek IMG, 6, 0;
		read IMG, $head, 4;
		close IMG;
		($width, $height) = unpack "vv", $head;
		return "GIF", $width, $height;
	}
	$head = substr $head, 0, 2;
	if ($head eq "\xff\xd8") {
		local($head, $width, $height, $w1, $w2, $h1, $h2, $l1, $l2, $length);
		seek IMG, 2, 0;
		while (read IMG, $head, 1) {
			last if ($head eq "");
			if ($head eq "\xff") {
				$head = getc IMG;
				if ($head =~ /^[\xc0-\xc3\xc5-\xcf]$/) {
					seek IMG, 3, 1;
					last if (read(IMG, $head, 4) != 4);
					close IMG;
					($h1, $h2, $w1, $w2) = unpack "C4", $head;
					$height = $h1 * 256 + $h2;
					$width  = $w1 * 256 + $w2;
					return "JPG", $width, $height;
				} elsif ($head eq "\xd9" || $head eq "\xda") {
					last;
				} else {
					last if (read(IMG, $head, 2) != 2);
					($l1, $l2) = unpack "CC", $head;
					$length = $l1 * 256 + $l2;
					seek IMG, $length - 2, 1;
				}
			}
		}
		close IMG;
		return "JPG", 0;
	}
	return 0;
}

###
sub crypt {
	@salt = ('a' .. 'z','A' .. 'Z','0' .. '9');
	srand;
	$salt = "$salt[int(rand($#salt))]$salt[int(rand($#salt))]";
	return crypt($_[0],$salt);
}

###
sub decrypt {
	$salt = $_[1] =~ /^\$1\$(.*)\$/ && $1 || substr($_[1],0,2);
	if (crypt($_[0],$salt) eq $_[1] || crypt($_[0],'$1$' . $salt) eq $_[1]) {return 1;}
	return 0;
}

###
sub error {
	if (!$head) {&header; print "<body><center>\n";}
	print "<br><br><br><br><h3>ERROR !!</h3><font color=red><b>$_[0]</b></font>\n";
	print "</center></body></html>\n";
	exit;
}
