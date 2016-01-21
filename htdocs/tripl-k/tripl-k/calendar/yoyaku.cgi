#!/usr/bin/perl --

#�� ̾������ ��ͽ������������� ver.1.6
#�� �⡡���� ��ͽ������򥫥�����������ɽ�����롣
#�� file  ̾ ��yoyaku.lzh
#�� ����� ��hige hige@deneb.freemail.ne.jp
#�� ��ԣȣ� ��CGI�Τ���Ť� http://www.dab.hi-ho.ne.jp/appletea/cgikan/
#�� ư��Ķ� ��Perl5
#�� library  ��jcode.pl��ɬ��
#�� �������� ��2001/02/07
#�� ����� �ۥե꡼���եȥ�����
#�� �� �� �� �������hige����ͭ���ޤ���
#�� ž�ܾ�� �۶ػ�

################################################################################
#
#	�����饤�֥�ꡧ�ѥ��Ͼ��ˤ�ä��ѹ�
#
################################################################################

require './jcode.pl';

################################################################################
#
#	ɬ���ѹ���������
#
################################################################################

#HOME(ͽ������������Ȥ�����)
$home = "http://triple-kmen.com/";

#�����ѥ����
$pwd = 'triplek';

################################################################################
#
#	���ˤ�ä��ѹ��������ꡧ�ǥ�����
#
################################################################################

####################################################################
# ɸ�५�������Ѥ����� (disptype=0/disptype����ʤ��ξ��Τ�ɬ��)

#������������(%���ꤹ����� type 1 �򻲹ͤ����ꤷ�Ƥ�������
#$calwidth = "100%"	#type 1
#$calwidth = 400;	#type 2
$calwidth = "80%";

####################################################################
# ��Ĺ���������Ѥ����� (disptype=1/2�ξ��Τ�ɬ��)

#1��������
$colwidth_day = 20;

#��̾ɽ��������
$colwidth_rowtitle = 90;

####################################################################
# ��������

#1���ξ��֤ο�(�㤨�и����ȸ����̡��˴�������Ȥ�->2)
#$periods = 1;
$periods = 3;

#1���ξ��֤ο���ʣ���ΤȤ��ˤ�����̤��뤿���ʸ����ɬ�פ���
#$showpname = 0;
$showpname = 1;

#1���ξ��֤ο���ʣ���ΤȤ��ˤ�����̤��뤿���ʸ����
#($showpname = 0 �λ�����������)
$periodname[0] = '1st';
$periodname[1] = '2nd';
$periodname[2] = '3rd';

#�طʿ�
$bgcolor = "#FFFFFF";

#���������η���ʬ
$caltitle_color = "#FFCC33";

#ʿ���ο�
$col[1] = "#FFFFFF";
$col[2] = "#FFFFFF";
$col[3] = "#FFFFFF";
$col[4] = "#FFFFFF";
$col[5] = "#FFFFFF";

#�������ο�
$col[6] = "#CCCCFF";

#�������ο�
$col[0] = "#FFCCCC";

#�����ο�
$col[7] = "#FFCCCC";

#���������Υǥե���Ƚ�
#�񼰤���������ʸ����ǯ�����������ʬ���ä��֤������ޤ�
#�����ǽ�ʽ񼰤ϲ������̤�Ǥ�����̣�Ͽ�¬���Ƥ���������(^^;
#  ǯ:YYYY,YY | ��:MM,M | ��:DD,D | ��:hh,h | ʬ:mm,m | ��:ss,s
$updtime_format = "YYYY.MM.DD";	# ex. 2001.07.07
#$updtime_format = "YY/M/D";	# ex. 01/7/7
#$updtime_format = "YY/M/D hh:mm";	# ex. 01/7/7 01:15

#�����ʹߤ�ͽ������Υǥե������
$default_stat = 0;

################################################################################
#
#	���ˤ�ä��ѹ��������ꡧ����¾
#
################################################################################

# OS��ʸ�������� (euc / sjis)
$os_code = 'euc';

# ���ϥ����� (euc / sjis)
$output_code = 'sjis';

#�ǡ����ե�����
$datafile = "./yoyaku/yoyaku.txt";

#ʸ����ե�����
$strfile = "./yoyaku/yoyakustr.txt";

#�����ե�����
$holidayfile = "./yoyaku/holiday.txt";

#��å��ѤΥǥ��쥯�ȥ�̾
$lockdir = "./yoyaku/yoyakulock";

#��������Ͽ�ե�����
$updfile = './yoyaku/upddate.txt';

################################################################################
#	�ѹ��ԲĤ�����

$self = $ENV{'SCRIPT_NAME'};

#����ʸ����
@wdaystr=  ('��', '��', '��', '��', '��', '��', '��');

#����
@days_leap   = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
@days_normal = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);

################################################################################
#
#	�¹Գ���
#
################################################################################

#�¹Գ���
&main;
exit;

################################################################################
#
#	�ᥤ��
#
################################################################################

#�ᥤ��ؿ�
sub main
{
	#�ե�����ǡ����Υǥ�����
	&form_decode;
	
	# ����ʸ�����åȤ����
	if ($output_code eq 'sjis')
	{
		$charset = 'Shift_JIS';
	}
	elsif ($output_code eq 'euc')
	{
		$charset = 'euc-jp';
	}

	#��Ĺ���������б��Τ��ᥫ���������򤳤���Ĵ��
	if ($FORM{'disptype'} == 1) {
		$calwidth = $colwidth_day * 31 + $colwidth_rowtitle;

		#��Ĵ��(�ơ��֥������������η�֤ʤɤ�ʬ��;�פˤȤ�)
		$calwidth = $calwidth
			+ 32 * 1 * 2	# 32���� * 1dot * ����
			+ 33 * 2;		# 33�� * 2dot

	} elsif ($FORM{'disptype'} == 2) {
		$calwidth = $colwidth_day * 16 + $colwidth_rowtitle;

		#��Ĵ��(�ơ��֥������������η�֤ʤɤ�ʬ��;�פˤȤ�)
		$calwidth = $calwidth
			+ 17 * 1 * 2	# 17���� * 1dot * ����
			+ 18 * 2;		# 18�� * 2dot
	}

	#����ʬ��
	if ($FORM{'mode'} eq 'show') {
		&show;
	} elsif ($FORM{'mode'} eq 'edit') {
		&edit;
	} elsif ($FORM{'mode'} eq 'save') {
		&save;
	} elsif ($FORM{'mode'} eq 'editstr') {
		&editstr;
	} elsif ($FORM{'mode'} eq 'savestr') {
		&savestr;
	} elsif ($FORM{'mode'} eq 'mng') {
		&mng;
	} elsif ($FORM{'mode'} eq 'ssishow') {
		&ssishow;
	} elsif ($FORM{'mode'} eq '') {
		&mng;
	} elsif ($FORM{'mode'} eq 'updtime') {
		&updtime;
	} else {
		&error("CGI���Ϥ��줿�ѥ�᡼���������Ǥ���");
	}
}

################################################################################
#
#	����Ū�ʴؿ�
#
################################################################################

#�ե�����ǡ����Υǥ�����
sub form_decode
{
	local($form);
	local(@pairs);
	local($name, $value);
	
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $form, $ENV{'CONTENT_LENGTH'});
	} else {
		$form = $ENV{'QUERY_STRING'};
	}

	@pairs = split(/&/,$form);

	foreach (@pairs) { 
		($name, $value) = split(/=/, $_);

		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		$value =~ s/>/&gt;/g;
		$value =~ s/</&lt;/g;

		&jcode'convert(*value, 'euc');
		&jcode'convert(*name, 'euc');

		$FORM{$name} = $value;
	} 
}

#HTML����
sub print_html
{
	local($html) = @_;
	
	&jcode'convert(*html, $output_code);

	print "Content-type: text/html\n\n";
	print $html;
}

#���뤦ǯȽ��
sub is_leap_year
{
	local($year) = @_;

	if ($year % 4 != 0) {
		return 0;
	} elsif ($year % 100 != 0) {
		return 1;
	} elsif ($year % 400 != 0) {
		return 0;
	} elsif ($year % 4000 != 0) {
		return 1;
	} else {
		return 0;
	}
}

#���������������
sub get_days
{
	local($year, $month) = @_;
	local($is_leap);
	
	#���뤦ǯ����
	$is_leap = is_leap_year($year, $month);
	
	#�������֤�
	if ($is_leap) {
		return $days_leap[$month];
	} else {
		return $days_normal[$month];
	}
}

#�����������������
sub get_wday
{
	local($year, $month, $day, $wday) = @_;

	if ($month <= 2) {
		$year--;
		$month += 12;
	}

	$wday = ($year + int($year/4) - int($year/100) + int($year/400) + int((13*$month + 8)/5) + $day) % 7;
	return $wday;
}

#��å�
sub lock
{
	local($lockdir) = @_;
	local($pre_time, $timeflag, $i, $rc);

	($pre_time) = (stat($lockdir))[9];

	$timeflag = time() - $pre_time;
	$i=1;

	while(1) {
		if (mkdir("$lockdir", 0755)) {
			$rc = 1;
			last;
		}

		if ($i == 1) {
			if ($timeflag > 300) {
				rmdir($lockdir);
			}
		} elsif ($i < 6) {
			sleep(1);
		} else {
			$rc = 0;
			last;
		}

		$i++;
	}

	return $rc;
}

#��å����
sub unlock
{
	local($lockdir) = @_;
	rmdir($lockdir);
}

################################################################################
#
#	�ץ������Ƕ��̤˻Ȥ������ʴؿ�
#
################################################################################

#�о�ǯ������
sub get_target_month
{
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	
	#���л��꤬����Ф����ͥ��
	if ($FORM{'next'} ne '') {
		#�����������
		$ENV{'TZ'} = "JST-9";
		($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
		$year = 1900 + $year;
		
		#����ɲ�
		$month += $FORM{'next'};
		
		#ǯ�η���
		$year += int($month / 12);
		$month = $month % 12;
		$month++;
		
		return ($year, $month);
	}

	#�ե�������Ϥ��줿ǯ���ʬ��
	($year, $month) = split(/\//, $FORM{'month'});

	#Ŭ���ϰ���Ǥ���Ф��Τޤ޺���(2000ǯ��2099ǯ������)
	if (($year > 1999) && ($year < 2100) && ($month > 0) && ($month < 13)) {
		return ($year, $month);
	}
	
	#Ŭ���ϰ���Ǥʤ���硢���ߤ�ǯ���������
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;
	
	return ($year, $month);
}

#����ʸ������ɤ߹���
sub read_strfile
{
	local($stat, $str, $longstr);
	
	#�ե�����򳫤�
	open(IN, $strfile);

	while (<IN>) {
		#�ǥ�����
		($stat, $str, $longstr) = split(/<>/,$_);

		#�����ǡ���������
		$STATUSSTR[$stat] = $str;
		$STATUSSTRL[$stat] = $longstr;
	}

	close(IN);
}

#�������ɤ߹���
sub read_holiday
{
	local($year, $month) = @_;
	local($y, $m, $d);

	#�����
	@HOLIDAY = ();

	#�ե�����򳫤�
	open(IN, $holidayfile);

	while (<IN>) {
		#�ǥ�����
		($y, $m, $d) = split(/\//,$_);

		#�����ǡ���������
		if (($y == $year) && ($m == $month)) {
			push(@HOLIDAY, $d);
		}
	}

	close(IN);
}

#�Ť��ǡ�����������
sub delete_old_data
{
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	
	#���ߤ����������
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;
	
	#yyyymmdd�η����Ѵ�
	local($datevalue) = $year * 10000 + $month * 100 + $mday;
	
	#��å�
	if (!&lock($lockdir)) {
		&error("��å������˼��Ԥ��ޤ�����");
		return;
	}
	
	#���ߤΥǡ������ɤ߹���(�Ť��ǡ����Ͻ���)
	local($y, $m, $d, $stat);
	
	open(IN, $datafile);

	while (<IN>) {
		#�ǥ�����
		($y, $m, $d, $stat) = split(/<>/, $_);

		#�����ǡ���������
		if (($y * 10000 + $m * 100 + $d) >= $datevalue) {
			push(@lines, $_);
		}
	}

	close(IN);
	
	#�ե�����򹹿�
	open(OUT, ">$datafile");
	print OUT @lines;
	close(OUT);
	
	#��å����
	&unlock($lockdir);
}

#����Ƚ��
sub is_holiday
{
	local($year, $month, $day) = @_;
	
	foreach (@HOLIDAY) {
		if ($day == $_) {
			return 1;
		}
	}

	return 0;
}
################################################################################
#
#	���顼ɽ��
#
################################################################################

#���顼
sub error
{
	local($msg) = @_;
	local($html);
	
	#��å������ν���
	if ($msg ne '') {
		$msg = "���顼��å�������<br>$msg";
	}
	
	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>���顼</title>
</head>
<body text="#333333" bgcolor="#ffffff">
<br>
CGI���顼��ȯ�����ޤ�����<br>
�֥饦���Ρ����פ����β��̤���äƤ���������<br>
<br>
$msg
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

################################################################################
#
#	ͽ��ɽ��
#
################################################################################

#ͽ��ɽ��
sub show
{
	local($html);
	local($calender);
	local($copyright);

	#�Ť��ǡ�������
	&delete_old_data;
	
	#�о�ǯ������
	local($year, $month) = &get_target_month();

	#����η�����
	local($prevyear, $prevmonth) = ($year, $month-1);
	local($nextyear, $nextmonth) = ($year, $month+1);
	
	if ($prevmonth == 0) {
		$prevyear--;
		$prevmonth = 12;
	}
	
	if ($nextmonth == 13) {
		$nextyear++;
		$nextmonth = 1;
	}
	
	#����ʸ��������
	&read_strfile;
	
	#���������
	&read_holiday($year, $month);

	#��������ɽ���������
	$calender = &get_calender($year, $month, 0);
	
	#���ɽ���������
	$copyright = &get_copyright;

	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>$yearǯ$month���ͽ�����</title>
<body bgcolor="$bgcolor">
<p><a href="$home">���</a></p>
<b>ͽ���������</b>
<hr>
<table border=0><tr><td valign="top">
<table border=0>
<tr><td>$STATUSSTR[1]</td><td>$STATUSSTRL[1]</td></tr>
<tr><td>$STATUSSTR[2]</td><td>$STATUSSTRL[2]</td></tr>
<tr><td>$STATUSSTR[3]</td><td>$STATUSSTRL[3]</td></tr>
</table>
</td><td valign="top">
<table border=0>
<tr><td>$STATUSSTR[0]</td><td>$STATUSSTRL[0]</td></tr>
<tr><td>$STATUSSTR[4]</td><td>$STATUSSTRL[4]</td></tr>
</table>
</td></tr></table>
$calender
<br>
<table border=0 width="$calwidth"><tr><td align="left">
<a href="$self?mode=show&month=$prevyear/$prevmonth&disptype=$FORM{'disptype'}"><< ���η�</a>
</td><td align="right">
<a href="$self?mode=show&month=$nextyear/$nextmonth&disptype=$FORM{'disptype'}">���η� >></a>
</td></tr></table>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

#��������ɽ���������
sub get_calender
{
	local($html) = '';
	local($year, $month, $edit) = @_;

	if ($FORM{'disptype'} == 1) {
		$html = &get_calender1($year, $month, $edit);
	} elsif ($FORM{'disptype'} == 2) {
		$html = &get_calender2($year, $month, $edit);
	} else {
		$html = &get_calender0($year, $month, $edit);
	}

	return $html;
}

#ɸ�५�����������פΥ������������
sub get_calender0
{
	local($html) = '';
	local($year, $month, $edit) = @_;
	local($day);
	local($i, $j, $k);
	local($days);
	local($firstwday);
	local($lastwday);
	local($holiday);

	#�оݥǡ��������
	&read_datafile($year, $month);
	
	#���������
	$days = &get_days($year, $month);
	
	#�ǽ�ȺǸ�����������
	$firstwday = &get_wday($year, $month, 1);
	$lastwday = &get_wday($year, $month, $days);
	
	#�����������Ȥη��˹�碌�ơ������ʬ������-1�ǽ����
	for ($i = 0; $i < $firstwday; $i++) {
		$calday[$i] = -1;
	}
	
	for ($i = 0; $i < $days; $i++) {
		$calday[$firstwday + $i] = $i+1;
	}
	
	for ($i = 0; $i < 6 - $lastwday; $i++) {
		$calday[$firstwday + $days + $i] = -1;
	}
	
	$caldays = $firstwday + $days + (6-$lastwday);
	
	#�ơ��֥볫��
	$html .= "<table border=1 cellspacing=0 width=\"$calwidth\">\n";
	$html .= "<tr><td colspan=7 align=\"center\" bgcolor=\"$caltitle_color\">$yearǯ$month��</td></tr>\n";
	
	#����̾
	$html .= "<tr>\n";
	
	for ($i = 0; $i < 7; $i++) {
		$html .= "<td align=\"center\" bgcolor=\"$col[$i]\">$wdaystr[$i]</td>\n";
	}
	
	$html .= "</tr>\n";
	
	#�����Ȥ�HTML����
	for ($i = 0; $i < $caldays / 7; $i++) {
		#����ɽ��
		$html .= "<tr>\n";

		for ($j = 0; $j < 7; $j++) {
			#���դ����
			$day = $calday[$i * 7 + $j];
			
			#�������դʤ����̤�ɽ������ʤ�����ʬ�Ȥ��ƽ���
			if ($day > 0) {
				$holiday = &is_holiday($year, $month, $day);

				if ($holiday) {
					$html .= "<td align=\"center\" bgcolor=\"$col[7]\">$day</td>\n";
				} else {
					$html .= "<td align=\"center\" bgcolor=\"$col[$j]\">$day</td>\n";
				}
			} else {
				$html .= "<td bgcolor=\"$col[$j]\">��</td>\n";
			}
		}

		$html .= "</tr>\n";

		#ͽ�����ɽ��
		$html .= "<tr>\n";

		for ($j = 0; $j < 7; $j++) {
			#���դ����
			$day = $calday[$i * 7 + $j];
			
			#�������դʤ����̤�ɽ������ʤ�����ʬ�Ȥ��ƽ���
			if ($day > 0) {
				@stats = split(/;/, $STATUS[$day]);

				#�Խ��⡼�ɰʳ���ɽ������������Խ��⡼�ɻ��ϥ���ܥܥå�����ɽ��
				if (!$edit) {
					$html .= "<td align=\"center\"><table width=\"100%\">";
					
					for ($l = 0; $l < $periods; $l++) {
						if ($showpname) { $html .= "<tr><td>$periodname[$l]</td>"; }
						$html .= "<td align=\"center\">$STATUSSTR[$stats[$l]]</td></tr>";
					}
					
					$html .= "</table></td>\n";
				} else {
					$html .= "<td align=\"center\">";
					
					for ($l = 0; $l < $periods; $l++) {
						if ($l == 0) {
							$selname = "stat$day";
						} else {
							$selname = "stat$day-$l";
						}
						
						$html .= "$periodname[$l]<select name=$selname>";

						for ($k = 0; $k < 5; $k++) {
							if ($stats[$l] == $k) {
								$html .= "<option value=\"$k\" selected>$STATUSSTR[$k]\n";
							} else {
								$html .= "<option value=\"$k\">$STATUSSTR[$k]\n";
							}
						}
						
						$html .= "</select><br>";
					}

					$html .= "</td>\n";
				}
			} else {
				$html .= "<td>��</td>";
			}
		}

		$html .= "</tr>\n";
	}
	
	#�ơ��֥뽪λ
	$html .= "</table>\n";

	return $html;
}

#��Ĺ�����פΥ������������
sub get_calender1
{
	local($html) = '';
	local($year, $month, $edit) = @_;
	local($day);
	local($days);
	local($firstwday);

	#�оݥǡ��������
	&read_datafile($year, $month);
	
	#���������
	$days = &get_days($year, $month);
	
	#�ǽ�����������
	$firstwday = &get_wday($year, $month, 1);
	
	# 1��
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 1, $days);

	return $html;
}

#��Ĺ������(�岼2��)�Υ������������
sub get_calender2
{
	local($html) = '';
	local($year, $month, $edit) = @_;
	local($days);
	local($firstwday);

	#�оݥǡ��������
	&read_datafile($year, $month);
	
	#���������
	$days = &get_days($year, $month);
	
	#�ǽ�����������
	$firstwday = &get_wday($year, $month, 1);
	
	# 1����
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 1, 16);
	$html .= "<br>";

	# 2����
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 17, $days);

	return $html;
}

# ��Ĺ����������1��ʬ
sub get_calender_row
{
	local($year, $month, $edit, $firstwday, $stday, $edday) = @_;
	local($html) = '';
	local($span);
	local($day);
	local($i, $j, $k);
	local($calwidth);
	local($holiday);

	#������������׻�(�ºݤˤ��Υơ��֥�˴ޤޤ�������˴�Ť����׻�)
	$calwidth = ($edday - $stday + 1) * $colwidth_day + $colwidth_rowtitle;

	#��Ĵ��
	$calwidth = $calwidth 
			+ ($edday - $stday + 2) * 1 * 2	# ����� * 1dot * ����
			+ ($edday - $stday + 3) * 2;	# �ܿ� * 2dot

	#ǯ������rowspan��׻�
	if ($showpname) {
		$span = 2;
	} else {
		$span = 2 + $periods;
	}

	#�ơ��֥볫��
	$html =<<"EOM";
<table border=1 cellspacing=0 width="$calwidth">
<tr><td rowspan=$span align="center" bgcolor="$caltitle_color" width="$colwidth_rowtitle">$yearǯ$month��</td>
EOM

	#����
	for ($i = $stday; $i <= $edday; $i++) {
		$day = $i;
		$wday = ($firstwday + $i - 1) % 7;
		$holiday = &is_holiday($year, $month, $day);

		if ($holiday) {
			$html .= "<td align=\"center\" bgcolor=\"$col[7]\" width=\"$colwidth_day\">$day</td>\n";
		} else {
			$html .= "<td align=\"center\" bgcolor=\"$col[$wday]\" width=\"$colwidth_day\">$day</td>\n";
		}
	}

	$html .= "</tr>\n";

	#����̾
	$html .= "<tr>\n";
	
	for ($i = $stday; $i <= $edday; $i++) {
		$day = $i;
		$wday = ($firstwday + $i - 1) % 7;
		$holiday = &is_holiday($year, $month, $day);

		if ($holiday) {
			$html .= "<td align=\"center\" bgcolor=\"$col[7]\" width=\"$colwidth_day\">$wdaystr[$wday]</td>\n";
		} else {
			$html .= "<td align=\"center\" bgcolor=\"$col[$wday]\" width=\"$colwidth_day\">$wdaystr[$wday]</td>\n";
		}
	}

	$html .= "</tr>\n";

	#�����Ȥ��Ȥ�HTML����
	for ($i = 0; $i < $periods; $i++) {
		$html .= "<tr>\n";

		#������̾
		if ($showpname) {
			$html .= "<td width=\"$colwidth_rowtitle\">$periodname[$i]</td>\n";
		}

		#�����Ȥ�HTML����
		for ($j = $stday; $j <= $edday; $j++) {
			$day = $j;
			@stats = split(/;/, $STATUS[$day]);

			#�Խ��⡼�ɰʳ���ɽ������������Խ��⡼�ɻ��ϥ���ܥܥå�����ɽ��
			if (!$edit) {
				$html .= "<td align=\"center\" width=\"$colwidth_day\">$STATUSSTR[$stats[$i]]</td>\n";
			} else {
				if ($i == 0) {
					$selname = "stat$day";
				} else {
					$selname = "stat$day-$i";
				}

				$html .= "<td><select name=$selname>";

				for ($k = 0; $k < 5; $k++) {
					if ($stats[$i] == $k) {
						$html .= "<option value=\"$k\" selected>$STATUSSTR[$k]\n";
					} else {
						$html .= "<option value=\"$k\">$STATUSSTR[$k]\n";
					}
				}
						
				$html .= "</select></td>\n";
			}
		}

		$html .= "</tr>\n";
	}

	#�ơ��֥뽪λ
	$html .= "</table>\n";

	return $html;
}

#�оݥǡ��������
sub read_datafile
{
	local($year, $month) = @_;
	local($y, $m, $d, $stat);
	local($i);
	
	#�����ʹߤν���ͤ����
	local($default_stat_1day) = '';
	
	for ($i = 0; $i < $periods; $i++) {
		$default_stat_1day .= $default_stat;
		$default_stat_1day .= ';';
	}

    #�����������
    $ENV{'TZ'} = "JST-9";
    local($sec,$min,$hour,$nd,$nm,$ny) = localtime(time);
    $ny = 1900 + $ny;
    $nm++;

	#�ǡ���������
	for ($i = 1; $i < 32; $i++) {
		$STATUS[$i] = 0;

        #�����ʹߤΥǡ���̤�������� $default_stat �ˤ���
        if (($year*10000+$month*100+$i) >= ($ny*10000+$nm*100+$nd)) {
            $STATUS[$i] = $default_stat_1day;
        }
	}
	
	#�ե�����򳫤�
	open(IN, $datafile);

	while (<IN>) {
		#�ǥ�����
		($y, $m, $d, $stat) = split(/<>/,$_);

		#�����ǡ���������
		if (($y == $year) && ($m == $month)) {
			$STATUS[$d] = $stat;
		}
	}

	close(IN);
}

################################################################################
#
#	ͽ��ɽ��(SSI�С������)
#
################################################################################

#ͽ��ɽ��
sub ssishow
{
	local($html);
	local($calender);
	
	#�Ť��ǡ�������
	&delete_old_data;
	
	#�о�ǯ������
	local($year, $month) = &get_target_month();

	#����η�����
	local($prevyear, $prevmonth) = ($year, $month-1);
	local($nextyear, $nextmonth) = ($year, $month+1);
	
	if ($prevmonth == 0) {
		$prevyear--;
		$prevmonth = 12;
	}
	
	if ($nextmonth == 13) {
		$nextyear++;
		$nextmonth = 1;
	}
	
	#����ʸ��������
	&read_strfile;
	
	#���������
	&read_holiday($year, $month);

	#��������ɽ���������
	$calender = &get_calender($year, $month, 0);
	
	#HTML����
	$html = $calender;

	#ɽ��
	&print_html($html);
}

################################################################################
#
#	ͽ���Խ�
#
################################################################################

#ͽ���Խ�
sub edit
{
	local($html);
	local($calender);
	local($copyright);

	#�ѥ���ɥ����å�
	if ($FORM{'pwd'} ne $pwd) {
		&error("�ѥ���ɤ��㤤�ޤ���");
		return;
	}
	
	#�о�ǯ������
	local($year, $month) = &get_target_month();

	#����ʸ��������
	&read_strfile;
	
	#���������
	&read_holiday($year, $month);

	#��������ɽ���������
	$calender = &get_calender($year, $month, 1);
	
	#���ɽ���������
	$copyright = &get_copyright;

	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>$yearǯ$month���ͽ�����:�Խ��⡼��</title>
</head>
<body bgcolor="$bgcolor">
<form action="$self" method=post>
<input type=hidden name=mode value="save">
<input type=hidden name=month value="$year/$month">
<input type=hidden name=pwd value="$FORM{'pwd'}">

<p><a href="$self?mode=mng&pwd=$FORM{'pwd'}">���</a></p>
<b>ͽ���������:�Խ��⡼��</b>
<hr>
<table border=0><tr><td valign="top">
<table border=0>
<tr><td>$STATUSSTR[1]</td><td>$STATUSSTRL[1]</td></tr>
<tr><td>$STATUSSTR[2]</td><td>$STATUSSTRL[2]</td></tr>
<tr><td>$STATUSSTR[3]</td><td>$STATUSSTRL[3]</td></tr>
</table>
</td><td valign="top">
<table border=0>
<tr><td>$STATUSSTR[0]</td><td>$STATUSSTRL[0]</td></tr>
<tr><td>$STATUSSTR[4]</td><td>$STATUSSTRL[4]</td></tr>
</table>
</td></tr></table>
$calender
<br>
<input type=submit value="����Ͽ���롡">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

################################################################################
#
#	ͽ����¸
#
################################################################################

#ͽ����¸
sub save
{
	local($html);
	local(@lines);
	
	#�ѥ���ɥ����å�
	if ($FORM{'pwd'} ne $pwd) {
		&error("�ѥ���ɤ��㤤�ޤ���");
		return;
	}

	#�о�ǯ������
	local($year, $month) = &get_target_month();

	#���������
	local($days) = &get_days($year, $month);
	
	#����ʬ�Υǡ�����񤭹��߲�ǽ�ʽ񼰤��Ѵ�
	local($day);
	local($tmpline);
	local($varname);
	
	for ($day = 1; $day < $days+1; $day++) {
		$stats = '';
		
		for ($l = 0; $l < $periods; $l++) {
			if ($l == 0) {
				$varname = "stat$day";
			} else {
				$varname = "stat$day-$l";
			}
			
			$stats .= "$FORM{$varname};";
		}

		$tmpline = "$year<>$month<>$day<>$stats<>\n";
		
		push(@lines, $tmpline);
	}

	#��å�
	if (!&lock($lockdir)) {
		&error("��å������˼��Ԥ��ޤ�����");
		return;
	}
	
	#���ߤΥǡ������ɤ߹���(�����оݤΥǡ����Ͻ���)
	local($y, $m, $d, $stat);
	
	open(IN, $datafile);

	while (<IN>) {
		#�ǥ�����
		($y, $m, $d, $stat) = split(/<>/, $_);

		#�����ǡ���������
		if (($y != $year) || ($m != $month)) {
			push(@lines, $_);
		}
	}

	close(IN);
	
	#�ե�����򹹿�
	open(OUT, ">$datafile");
	print OUT @lines;
	close(OUT);
	
	#��������Ͽ�ե�����򹹿�
	open(OUT, ">$updfile");
	print OUT "dummy text";
	close(OUT);

	#��å����
	&unlock($lockdir);
	
	#�������̤����
	&mng;
}

################################################################################
#
#	ʸ������Խ�
#
################################################################################

#ʸ������Խ�
sub editstr
{
	local($html);
	local($copyright);

	#�ѥ���ɥ����å�
	if ($FORM{'pwd'} ne $pwd) {
		&error("�ѥ���ɤ��㤤�ޤ���");
		return;
	}
	
	#����ʸ��������
	&read_strfile;

	#���ɽ���������
	$copyright = &get_copyright;

	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>����ʸ������Խ�</title>
</head>
<body bgcolor="$bgcolor">
<form action="$self" method=post>
<input type=hidden name=mode value="savestr">
<input type=hidden name=pwd value="$FORM{'pwd'}">

<p><a href="$self?mode=mng&pwd=$FORM{'pwd'}">���</a></p>
<b>����ʸ������Խ�</b>
<hr>
<table border=0>

<tr><td><b>����</b></td><td><b>����</b></td><td><b>��������������ʸ��</b></td></tr>

<tr><td>����������Ȥ�</td>
<td><input type=text name=str1 value="$STATUSSTR[1]" size=10></td>
<td><input type=text name=strl1 value="$STATUSSTRL[1]" size=30></td></tr>

<tr><td>���������ʤ��Ȥ�</td>
<td><input type=text name=str2 value="$STATUSSTR[2]" size=10></td>
<td><input type=text name=strl2 value="$STATUSSTRL[2]" size=30></td></tr>

<tr><td>�������ʤ��Ȥ�</td>
<td><input type=text name=str3 value="$STATUSSTR[3]" size=10></td>
<td><input type=text name=strl3 value="$STATUSSTRL[3]" size=30></td></tr>

<tr><td>̤����</td>
<td><input type=text name=str0 value="$STATUSSTR[0]" size=10></td>
<td><input type=text name=strl0 value="$STATUSSTRL[0]" size=30></td></tr>

<tr><td>���䤤��碌</td>
<td><input type=text name=str4 value="$STATUSSTR[4]" size=10></td>
<td><input type=text name=strl4 value="$STATUSSTRL[4]" size=30></td></tr>

</table>
<br>
<input type=submit value="����Ͽ���롡">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

################################################################################
#
#	ʸ������Խ�����¸
#
################################################################################

#ʸ������Խ�����¸
sub savestr
{
	#�ѥ���ɥ����å�
	if ($FORM{'pwd'} ne $pwd) {
		&error("�ѥ���ɤ��㤤�ޤ���");
		return;
	}
	
	#�������ǡ��������
	local(@lines);
	
	push(@lines, "0<>$FORM{'str0'}<>$FORM{'strl0'}<>\n");
	push(@lines, "1<>$FORM{'str1'}<>$FORM{'strl1'}<>\n");
	push(@lines, "2<>$FORM{'str2'}<>$FORM{'strl2'}<>\n");
	push(@lines, "3<>$FORM{'str3'}<>$FORM{'strl3'}<>\n");
	push(@lines, "4<>$FORM{'str4'}<>$FORM{'strl4'}<>\n");
	

	#��å�
	if (!&lock($lockdir)) {
		&error("��å������˼��Ԥ��ޤ�����");
		return;
	}
	
	#�ե�����򹹿�
	open(OUT, ">$strfile");
	print OUT @lines;
	close(OUT);
	
	#��å����
	&unlock($lockdir);
	
	#�������̤����
	&mng;
}

################################################################################
#
#	��������
#
################################################################################

#��������
sub mng
{
	local($html);
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	local($copyright);

	#�ѥ���ɤ����ꤵ��Ƥ��ʤ����ϥѥ�������ϲ��̤�ɽ��
	if ($FORM{'pwd'} eq '') {
		&pwd_input;
		return;
	}

	#�ѥ���ɥ����å�
	if ($FORM{'pwd'} ne $pwd) {
		&error("�ѥ���ɤ��㤤�ޤ���");
		return;
	}
	
	#���ߤ����������
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;

	#���ɽ���������
	$copyright = &get_copyright;

	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>ͽ�������������</title>
</head>
<body bgcolor="$bgcolor">
<p><a href="$home">���</a></p>
<b>ͽ�������������</b>
<hr>
<p>�� ͽ��������Խ�</p>
<form action="$self" method=post>
<input type=hidden name=mode value="edit">
<input type=hidden name=pwd value=$FORM{'pwd'}>
ǯ/���<input type=text name=month value="$year/$month" size=10>
��
<input type=radio name="disptype" value="0" checked>ɸ�ࡡ
<input type=radio name="disptype" value="1">��Ĺ1�ʡ�
<input type=radio name="disptype" value="2">��Ĺ2��<br><br>
<input type=submit value="�Խ�">
</form>
<p>�� ͽ�����ʸ�����Խ�</p>
<form action="$self" method=post>
<input type=hidden name=mode value="editstr">
<input type=hidden name=pwd value=$FORM{'pwd'}>
<input type=submit value="�Խ�">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

#�ѥ�������ϲ���
sub pwd_input
{
	local($html) = '';
	
	#HTML����
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>�ѥ��������</title>
</head>
<body text="#333333" bgcolor="#ffffff">
<br>
<hr>
<form action="$self" method=post>
�ѥ���ɡ�<input type=password name=pwd>
<input type=submit value="��������">
</form>
<hr>
</body>
</html>
EOM

	#ɽ��
	&print_html($html);
}

################################################################################
#
#	�������μ���
#
################################################################################

#����������SSI��ɽ��
sub updtime
{
	local($html);
	local($updtime);
	
	#�ե�����ι����������
	$updtime = &get_upddate($updfile);
	
	#HTML����
	$html = $updtime;

	#ɽ��
	&print_html($html);
}

#�ե�����ι����������
sub get_upddate
{
	local($file) = @_;
	local($updtime) = $updtime_format;
	local($tmp);
	
	#�ƤӽФ����˽񼰻��꤬����Ф����ͥ��
	if ($FORM{'fmt'} ne '') {
		$updtime = $FORM{'fmt'};
	}
	
	#�ե�����ι����������
	local($mtime) = (stat($file))[9];
	local($s,$m,$h,$day,$mon,$year) = localtime($mtime);

	#localtime���ͤ�Ĵ��
	$year = 1900 + $year;
	$mon++;
	
	#ǯ(YYYY)
	$updtime =~ s/YYYY/$year/;
	
	#ǯ(YY)
	$tmp = sprintf("%02d", $year % 100);
	$updtime =~ s/YY/$tmp/;
	
	#��(MM)
	$tmp = sprintf("%02d", $mon);
	$updtime =~ s/MM/$tmp/;
	
	#��(M)
	$updtime =~ s/M/$mon/;
	
	#��(DD)
	$tmp = sprintf("%02d", $day);
	$updtime =~ s/DD/$tmp/;
	
	#��(D)
	$updtime =~ s/D/$day/;
	
	#��(hh)
	$tmp = sprintf("%02d", $h);
	$updtime =~ s/hh/$tmp/;
	
	#��(h)
	$updtime =~ s/h/$h/;

	#ʬ(mm)
	$tmp = sprintf("%02d", $m);
	$updtime =~ s/mm/$tmp/;
	
	#ʬ(m)
	$updtime =~ s/m/$m/;

	#��(ss)
	$tmp = sprintf("%02d", $s);
	$updtime =~ s/ss/$tmp/;
	
	#��(s)
	$updtime =~ s/s/$s/;

	return $updtime;
}

################################################################################
#
#	���ɽ���μ���
#
################################################################################

#���ɽ���μ���
sub get_copyright
{
	#���
	local($copyright) = << "EOM";
<table border=0 width="$calwidth"><tr><td align="center">
- <a href="http://www.dab.hi-ho.ne.jp/appletea/cgikan/" 
target="_blank">CGI��:CGI�Τ���Ť�</a> -
</td></tr></table>
EOM

	return $copyright;
}

################################################################################
