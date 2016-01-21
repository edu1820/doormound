#!/usr/bin/perl

###############################################
#   inf14.cgi
#      V1.0 (2008.7.25)
#                     Copyright(C) CGI-design
###############################################

$script = 'inf14.cgi';
$base = './infdata';				#データ格納ディレクトリ
$inffile = "$base/inf.txt";			#記事
$nofile = "$base/no.txt";			#記事番号
$opfile = "$base/option.txt";

open (IN,"$opfile") || &error("OPEN ERROR");	$opdata = <IN>;		close IN;
if (!$opdata) {
	$pass = &crypt('cgi');
	chmod(0666,$opfile);	open (OUT,">$opfile") || &error("OPEN ERROR");
	print OUT "$pass<>#7eaedf,#ffffff,#000000,#ffffff<>5<>620";
	close OUT;
	chmod(0666,$inffile);	chmod(0666,$nofile);
}

###　メイン処理　###
if ($ENV{'REQUEST_METHOD'} eq "POST") {read(STDIN,$in,$ENV{'CONTENT_LENGTH'});} else {$in = $ENV{'QUERY_STRING'};}
%in = ();
foreach (split(/&/,$in)) {
	($n,$val) = split(/=/);
	$val =~ tr/+/ /;
	$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$val =~ s/&/&amp;/g;	$val =~ s/</&lt;/g;		$val =~ s/>/&gt;/g;		$val =~ s/"/&quot;/g;	$val =~ s/\r\n|\r|\n/<br>/g;
	if (defined($in{$n})) {$in{$n} .= "\0$val";} else {$in{$n} = $val;}
}
$mode = $in{'mode'};
$num = $in{'num'};

open (IN,"$opfile") || &error("OPEN ERROR");
($pass,$colors,$page,$dspw) = split(/<>/,<IN>);
close IN;
($frame_color,$sub_color,$com_color,$combg_color) = split(/,/,$colors);
if ($page == 0) {$page = 5;}

if ($mode eq 'admin') {&admin;} else {&main;}
exit;

###
sub header {
	print "Content-type: text/html\n\n";
	print "<html><head><META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print "<title>管理</title><link rel=\"stylesheet\" type=\"text/css\" href=\"$base/style.css\"></head>\n";
	$head = 1;
}

###
sub main {
	$htmp = '';
	open (IN,"temp.html") || &error("OPEN ERROR");		while (<IN>) {$htmp .= $_;}		close IN;
	($htmp,$ftmp) = split(/!cgidata/,$htmp);

	print "Content-type: text/html\n\n";
	print $htmp;
	$head = 1;
	&dsp;
	if (0 <= $back) {print "<a href=\"$script?num=$back\">&lt;&lt; 前ページ</a>　　";}
	if ($next <= $m) {print "<a href=\"$script?num=$next\">次ページ &gt;&gt;</a>";}
	# 次の行は著作権表示ですので削除しないで下さい。#
	print "<div align=right><a href=\"http://cgi-design.net\" target=\"_blank\">CGI-design</a>&nbsp;</div>\n";
	print $ftmp;
}

###
sub dsp {
	$back = $num - $page;
	$next = $num + $page;
	$m = -1;
	open (IN,"$inffile") || &error("OPEN ERROR");
	while (<IN>) {
		$m++;
		if ($m < $num) {next;}
		if ($next <= $m) {last;}

		($no,$sub,$com) = split(/<>/);
		$com =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
		print "<table width=$dspw bgcolor=\"$frame_color\" cellspacing=2 cellpadding=3>\n";
		print "<tr><td>　<font color=\"$sub_color\"><b>$sub</b></font></td><td align=right>";
		if ($mode eq 'admin') {print "<input type=submit name=$no value=\"修正\">";}
		print "</td></tr>\n";
		print "<tr><td bgcolor=\"$combg_color\" colspan=2 style=\"padding: 5px;\">\n";
		print "<font color=\"$com_color\">$com</font></td></tr></table><br>\n";
	}
	close IN;
}

###
sub admin {
	&header;
	print "<body><center>\n";
	$inpass = $in{'pass'};
	if ($inpass eq '') {
		print "<table width=97%><tr><td><a href=\"$script\">[Return]</a></td></tr></table>\n";
		print "<br><br><br><br><h4>パスワードを入力して下さい</h4>\n";
		print "<form action=\"$script\" method=POST>\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=password size=10 maxlength=8 name=pass>\n";
		print " <input type=submit value=\" 認証 \"></form>\n";
		print "</center></body></html>\n";
		exit;
	}
	$mat = &decrypt($inpass,$pass);
	if (!$mat) {&error("パスワードが違います");}

	print "<table width=95% bgcolor=\"#8c4600\"><tr><td>　<a href=\"$script\"><font color=\"#ffffff\"><b>Return</b></font></a></td>\n";
	print "<form action=\"$script\" method=POST><td align=right>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=submit value=\"新規/修正\">\n";
	print "<input type=submit name=set value=\"基本設定\"></td></form><td width=10></td></tr></table><br>\n";

	if ($in{'set'}) {&setup;} else {&edtin;}

	print "</center></body></html>\n";
}

###
sub edtin {
	if ($in{'newwrt'}) {&newwrt;}
	elsif ($in{'edtwrt'}) {&edtwrt;}
	elsif ($in{'delwrt'}) {&delwrt;}

	&in_form;
	print "<form action=\"$script\" method=POST>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=edt value=\"1\">\n";
	print "<input type=hidden name=num value=\"$num\">\n";
	print "<hr width=700>修正、削除する場合は「修正」をクリックして下さい。<div style=\"margin-top:5px;\"></div>\n";
	&dsp;
	print "</form>\n";

	print "<table cellpadding=0><tr>\n";
	if (0 <= $back) {
		print "<form action=\"$script\" method=POST><td width=80>\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=pass value=\"$inpass\">\n";
		print "<input type=hidden name=num value=\"$back\">\n";
		print "<input type=submit value=\"前ページ\"></td></form>\n";
	}
	if ($next <= $m) {
		print "<form action=\"$script\" method=POST><td>\n";
		print "<input type=hidden name=mode value=\"admin\">\n";
		print "<input type=hidden name=pass value=\"$inpass\">\n";
		print "<input type=hidden name=num value=\"$next\">\n";
		print "<input type=submit value=\"次ページ\"></td></form>\n";
	}
	print "</tr></table>\n";
}

###
sub in_form {
	print "<form action=\"$script\" method=POST>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	if ($in{'edt'}) {
		open (IN,"$inffile") || &error("OPEN ERROR");
		while (<IN>) {
			($no,$sub,$com) = split(/<>/);
			if ($in{$no}) {last;}
		}
		close IN;
		print "<input type=hidden name=no value=\"$no\">\n";
		print "<input type=hidden name=num value=\"$num\">\n";
		$com =~ s/<br>/\r/g;
	} else {$sub=$com='';}
	print "<table bgcolor=\"#e6e4ce\" cellspacing=10><tr><td><table cellspacing=1 cellpadding=0>\n";
	print "<tr><td>題名&nbsp;</td><td><input type=text size=70 name=sub value=\"$sub\" style=\"ime-mode:active;\"></td></tr>\n";
	print "<tr><td valign=top><br>内容</td><td><textarea cols=80 rows=12 name=com style=\"ime-mode:active;\">$com</textarea></td></tr>\n";
	print "<tr><td></td><td>";
	if ($in{'edt'}) {
		print "<table width=100%><tr><td><input type=submit name=edtwrt value=\"修正する\"></td>\n";
		print "<td width=40 bgcolor=red align=center><input type=submit name=delwrt value=\"削除\"></td></tr></table>\n";
	} else {print "<input type=submit name=newwrt value=\"新規登録\">";}
	print "</td></tr></table></td></tr></table></form>\n";
}

###
sub newwrt {
	open (IN,"$nofile") || &error("OPEN ERROR"); 		$no = <IN>; 		close IN;
	$no++;
	open (OUT,">$nofile") || &error("OPEN ERROR");		print OUT $no;		close OUT;

	open (IN,"$inffile") || &error("OPEN ERROR");		@new = <IN>;		close IN;
	unshift(@new,"$no<>$in{'sub'}<>$in{'com'}<>\n");
	open (OUT,">$inffile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
}

###
sub edtwrt {
	@new = ();
	open (IN,"$inffile") || &error("OPEN ERROR");
	while (<IN>) {
		($no) = split(/<>/);
		if ($no eq $in{'no'}) {push(@new,"$no<>$in{'sub'}<>$in{'com'}<>\n");} else {push(@new,$_);}
	}
	close IN;
	open (OUT,">$inffile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
}

###
sub delwrt {
	@new = ();
	open (IN,"$inffile") || &error("OPEN ERROR");
	while (<IN>) {
		($no) = split(/<>/);
		if ($no ne $in{'no'}) {push(@new,$_);}
	}
	close IN;
	open (OUT,">$inffile") || &error("OPEN ERROR");		print OUT @new;		close OUT;
}

###
sub setup {
	if ($in{'wrt'}) {
		if ($in{'newpass'} ne '') {$pass = &crypt($in{'newpass'});}
		$colors = $in{'colors'};	$colors =~ s/\0/,/g;
		$page = $in{'page'};		$dspw = $in{'dspw'};

		open (OUT,">$opfile") || &error("OPEN ERROR");
		print OUT "$pass<>$colors<>$page<>$dspw";
		close OUT;
	}
	print "下記に入力後、「設定する」を押して下さい。<br><br>\n";
	print "<form action=\"$script\" method=POST>\n";
	print "<input type=hidden name=mode value=\"admin\">\n";
	print "<input type=hidden name=pass value=\"$inpass\">\n";
	print "<input type=hidden name=set value=\"1\">\n";
	print "<input type=submit name=wrt value=\"設定する\"><br><br>\n";

	print "<table bgcolor=\"#dddddd\" cellspacing=10><tr><td><table cellspacing=1 cellpadding=0>\n";
	print "<tr><td></td><td><a href=\"$base/color.htm\" target=\"_blank\">カラーコード</a></td></tr>\n";
	@name = ('枠色','題名色','内容色','内容背景色');
	@colors = split(/,/,$colors);
	for (0 .. $#name) {
		print "<tr><td><b>$name[$_]</b></td><td><table cellspacing=0 cellpadding=0><tr>\n";
		print "<td><input type=text size=10 name=colors value=\"$colors[$_]\" style=\"ime-mode:inactive;\"></td>\n";
		print "<td width=5></td><td width=80 bgcolor=\"$colors[$_]\"></td></tr></table></td></tr>\n";
	}
	print "<tr><td><b>記事表\示</b></td><td><input type=text size=3 name=page value=\"$page\" style=\"text-align:right; ime-mode:disabled;\">件/ページ　　表\示幅<input type=text size=4 name=dspw value=\"$dspw\" style=\"text-align:right; ime-mode:disabled;\">px</td></tr>\n";
	print "<tr><td><b>パスワード変更</b></td><td><input type=password size=10 maxlength=8 name=newpass> （英数8文字以内）</td></tr>\n";
	print "</table></td></tr></table></form>\n";
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
	if (!$head) {&header; print "<body><center>";}
	print "<br><br><br><br><h3>ERROR !!</h3><font color=red><b>$_[0]</b></font>\n";
	print "</center></body></html>\n";
	exit;
}
