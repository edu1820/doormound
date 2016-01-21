#!/usr/bin/perl --

#【 名　　称 】予約状況カレンダー ver.1.6
#【 説　　明 】予約状況をカレンダー形式で表示する。
#【 file  名 】yoyaku.lzh
#【 作　　者 】hige hige@deneb.freemail.ne.jp
#【 作者ＨＰ 】CGIのかんづめ http://www.dab.hi-ho.ne.jp/appletea/cgikan/
#【 動作環境 】Perl5
#【 library  】jcode.plが必要
#【 作成月日 】2001/02/07
#【 種　　別 】フリーソフトウェア
#【 著 作 権 】著作権はhigeが保有します。
#【 転載条件 】禁止

################################################################################
#
#	外部ライブラリ：パスは場合によって変更
#
################################################################################

require './jcode.pl';

################################################################################
#
#	必ず変更する設定
#
################################################################################

#HOME(予約状況から戻るときの頁)
$home = "http://triple-kmen.com/";

#管理パスワード
$pwd = 'triplek';

################################################################################
#
#	場合によって変更する設定：デザイン
#
################################################################################

####################################################################
# 標準カレンダー用の設定 (disptype=0/disptype指定なしの場合のみ必要)

#カレンダーの幅(%指定する場合は type 1 を参考に設定してください
#$calwidth = "100%"	#type 1
#$calwidth = 400;	#type 2
$calwidth = "80%";

####################################################################
# 横長カレンダー用の設定 (disptype=1/2の場合のみ必要)

#1日の列幅
$colwidth_day = 20;

#列名表示の列幅
$colwidth_rowtitle = 90;

####################################################################
# 共通設定

#1日の状態の数(例えば午前と午後を別々に管理するとき->2)
#$periods = 1;
$periods = 3;

#1日の状態の数が複数のときにそれを識別するための文字列が必要か？
#$showpname = 0;
$showpname = 1;

#1日の状態の数が複数のときにそれを識別するための文字列
#($showpname = 0 の時は設定不要)
$periodname[0] = '1st';
$periodname[1] = '2nd';
$periodname[2] = '3rd';

#背景色
$bgcolor = "#FFFFFF";

#カレンダーの月部分
$caltitle_color = "#FFCC33";

#平日の色
$col[1] = "#FFFFFF";
$col[2] = "#FFFFFF";
$col[3] = "#FFFFFF";
$col[4] = "#FFFFFF";
$col[5] = "#FFFFFF";

#土曜日の色
$col[6] = "#CCCCFF";

#日曜日の色
$col[0] = "#FFCCCC";

#祝日の色
$col[7] = "#FFCCCC";

#更新日時のデフォルト書式
#書式の中の特定の文字が年、月、日、時、分、秒と置き換わります
#指定可能な書式は下記の通りです。意味は推測してください。(^^;
#  年:YYYY,YY | 月:MM,M | 日:DD,D | 時:hh,h | 分:mm,m | 秒:ss,s
$updtime_format = "YYYY.MM.DD";	# ex. 2001.07.07
#$updtime_format = "YY/M/D";	# ex. 01/7/7
#$updtime_format = "YY/M/D hh:mm";	# ex. 01/7/7 01:15

#今日以降の予約状況のデフォルト値
$default_stat = 0;

################################################################################
#
#	場合によって変更する設定：その他
#
################################################################################

# OSの文字コード (euc / sjis)
$os_code = 'euc';

# 出力コード (euc / sjis)
$output_code = 'sjis';

#データファイル
$datafile = "./yoyaku/yoyaku.txt";

#文字列ファイル
$strfile = "./yoyaku/yoyakustr.txt";

#祝日ファイル
$holidayfile = "./yoyaku/holiday.txt";

#ロック用のディレクトリ名
$lockdir = "./yoyaku/yoyakulock";

#更新日記録ファイル
$updfile = './yoyaku/upddate.txt';

################################################################################
#	変更不可の設定

$self = $ENV{'SCRIPT_NAME'};

#曜日文字列
@wdaystr=  ('日', '月', '火', '水', '木', '金', '土');

#日数
@days_leap   = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
@days_normal = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);

################################################################################
#
#	実行開始
#
################################################################################

#実行開始
&main;
exit;

################################################################################
#
#	メイン
#
################################################################################

#メイン関数
sub main
{
	#フォームデータのデコード
	&form_decode;
	
	# 出力文字セットを決定
	if ($output_code eq 'sjis')
	{
		$charset = 'Shift_JIS';
	}
	elsif ($output_code eq 'euc')
	{
		$charset = 'euc-jp';
	}

	#横長カレンダー対応のためカレンダー幅をここで調整
	if ($FORM{'disptype'} == 1) {
		$calwidth = $colwidth_day * 31 + $colwidth_rowtitle;

		#微調整(テーブルの線幅、セルの隙間などの分を余計にとる)
		$calwidth = $calwidth
			+ 32 * 1 * 2	# 32セル * 1dot * 左右
			+ 33 * 2;		# 33本 * 2dot

	} elsif ($FORM{'disptype'} == 2) {
		$calwidth = $colwidth_day * 16 + $colwidth_rowtitle;

		#微調整(テーブルの線幅、セルの隙間などの分を余計にとる)
		$calwidth = $calwidth
			+ 17 * 1 * 2	# 17セル * 1dot * 左右
			+ 18 * 2;		# 18本 * 2dot
	}

	#処理分岐
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
		&error("CGIに渡されたパラメータが不正です。");
	}
}

################################################################################
#
#	汎用的な関数
#
################################################################################

#フォームデータのデコード
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

#HTML出力
sub print_html
{
	local($html) = @_;
	
	&jcode'convert(*html, $output_code);

	print "Content-type: text/html\n\n";
	print $html;
}

#うるう年判定
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

#指定月の日数を取得
sub get_days
{
	local($year, $month) = @_;
	local($is_leap);
	
	#うるう年か？
	$is_leap = is_leap_year($year, $month);
	
	#日数を返す
	if ($is_leap) {
		return $days_leap[$month];
	} else {
		return $days_normal[$month];
	}
}

#指定日の曜日を取得
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

#ロック
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

#ロック解除
sub unlock
{
	local($lockdir) = @_;
	rmdir($lockdir);
}

################################################################################
#
#	プログラム内で共通に使えそうな関数
#
################################################################################

#対象年月を取得
sub get_target_month
{
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	
	#相対指定があればそれを優先
	if ($FORM{'next'} ne '') {
		#現在日を取得
		$ENV{'TZ'} = "JST-9";
		($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
		$year = 1900 + $year;
		
		#月を追加
		$month += $FORM{'next'};
		
		#年の繰越
		$year += int($month / 12);
		$month = $month % 12;
		$month++;
		
		return ($year, $month);
	}

	#フォームで渡された年月を分解
	($year, $month) = split(/\//, $FORM{'month'});

	#適正範囲内であればそのまま採用(2000年〜2099年を想定)
	if (($year > 1999) && ($year < 2100) && ($month > 0) && ($month < 13)) {
		return ($year, $month);
	}
	
	#適正範囲内でない場合、現在の年月日を採用
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;
	
	return ($year, $month);
}

#状態文字列を読み込む
sub read_strfile
{
	local($stat, $str, $longstr);
	
	#ファイルを開く
	open(IN, $strfile);

	while (<IN>) {
		#デコード
		($stat, $str, $longstr) = split(/<>/,$_);

		#該当データを設定
		$STATUSSTR[$stat] = $str;
		$STATUSSTRL[$stat] = $longstr;
	}

	close(IN);
}

#祝日を読み込む
sub read_holiday
{
	local($year, $month) = @_;
	local($y, $m, $d);

	#初期化
	@HOLIDAY = ();

	#ファイルを開く
	open(IN, $holidayfile);

	while (<IN>) {
		#デコード
		($y, $m, $d) = split(/\//,$_);

		#該当データを設定
		if (($y == $year) && ($m == $month)) {
			push(@HOLIDAY, $d);
		}
	}

	close(IN);
}

#古いデータを削除する
sub delete_old_data
{
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	
	#現在の日時を取得
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;
	
	#yyyymmddの形に変換
	local($datevalue) = $year * 10000 + $month * 100 + $mday;
	
	#ロック
	if (!&lock($lockdir)) {
		&error("ロック処理に失敗しました。");
		return;
	}
	
	#現在のデータを読み込む(古いデータは除く)
	local($y, $m, $d, $stat);
	
	open(IN, $datafile);

	while (<IN>) {
		#デコード
		($y, $m, $d, $stat) = split(/<>/, $_);

		#該当データを設定
		if (($y * 10000 + $m * 100 + $d) >= $datevalue) {
			push(@lines, $_);
		}
	}

	close(IN);
	
	#ファイルを更新
	open(OUT, ">$datafile");
	print OUT @lines;
	close(OUT);
	
	#ロック解除
	&unlock($lockdir);
}

#祝日判定
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
#	エラー表示
#
################################################################################

#エラー
sub error
{
	local($msg) = @_;
	local($html);
	
	#メッセージの処理
	if ($msg ne '') {
		$msg = "エラーメッセージ：<br>$msg";
	}
	
	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>エラー</title>
</head>
<body text="#333333" bgcolor="#ffffff">
<br>
CGIエラーが発生しました。<br>
ブラウザの「戻る」で前の画面に戻ってください。<br>
<br>
$msg
</body>
</html>
EOM

	#表示
	&print_html($html);
}

################################################################################
#
#	予約表示
#
################################################################################

#予約表示
sub show
{
	local($html);
	local($calender);
	local($copyright);

	#古いデータを削除
	&delete_old_data;
	
	#対象年月を取得
	local($year, $month) = &get_target_month();

	#前後の月を取得
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
	
	#状態文字列を取得
	&read_strfile;
	
	#祝日を取得
	&read_holiday($year, $month);

	#カレンダー表示部を取得
	$calender = &get_calender($year, $month, 0);
	
	#著作権表示部を取得
	$copyright = &get_copyright;

	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>$year年$month月の予約状況</title>
<body bgcolor="$bgcolor">
<p><a href="$home">戻る</a></p>
<b>予約状況一覧</b>
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
<a href="$self?mode=show&month=$prevyear/$prevmonth&disptype=$FORM{'disptype'}"><< 前の月</a>
</td><td align="right">
<a href="$self?mode=show&month=$nextyear/$nextmonth&disptype=$FORM{'disptype'}">次の月 >></a>
</td></tr></table>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#表示
	&print_html($html);
}

#カレンダー表示部を取得
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

#標準カレンダータイプのカレンダーを取得
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

	#対象データを取得
	&read_datafile($year, $month);
	
	#日数を取得
	$days = &get_days($year, $month);
	
	#最初と最後の曜日を取得
	$firstwday = &get_wday($year, $month, 1);
	$lastwday = &get_wday($year, $month, $days);
	
	#カレンダーの枠の形に合わせて、隙間部分の日を-1で初期化
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
	
	#テーブル開始
	$html .= "<table border=1 cellspacing=0 width=\"$calwidth\">\n";
	$html .= "<tr><td colspan=7 align=\"center\" bgcolor=\"$caltitle_color\">$year年$month月</td></tr>\n";
	
	#曜日名
	$html .= "<tr>\n";
	
	for ($i = 0; $i < 7; $i++) {
		$html .= "<td align=\"center\" bgcolor=\"$col[$i]\">$wdaystr[$i]</td>\n";
	}
	
	$html .= "</tr>\n";
	
	#週ごとにHTML作成
	for ($i = 0; $i < $caldays / 7; $i++) {
		#日付表示
		$html .= "<tr>\n";

		for ($j = 0; $j < 7; $j++) {
			#日付を取得
			$day = $calday[$i * 7 + $j];
			
			#正の日付なら普通に表示・負なら隙間部分として処理
			if ($day > 0) {
				$holiday = &is_holiday($year, $month, $day);

				if ($holiday) {
					$html .= "<td align=\"center\" bgcolor=\"$col[7]\">$day</td>\n";
				} else {
					$html .= "<td align=\"center\" bgcolor=\"$col[$j]\">$day</td>\n";
				}
			} else {
				$html .= "<td bgcolor=\"$col[$j]\">　</td>\n";
			}
		}

		$html .= "</tr>\n";

		#予約状況表示
		$html .= "<tr>\n";

		for ($j = 0; $j < 7; $j++) {
			#日付を取得
			$day = $calday[$i * 7 + $j];
			
			#正の日付なら普通に表示・負なら隙間部分として処理
			if ($day > 0) {
				@stats = split(/;/, $STATUS[$day]);

				#編集モード以外は表示するだけ、編集モード時はコンボボックスで表示
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
				$html .= "<td>　</td>";
			}
		}

		$html .= "</tr>\n";
	}
	
	#テーブル終了
	$html .= "</table>\n";

	return $html;
}

#横長タイプのカレンダーを取得
sub get_calender1
{
	local($html) = '';
	local($year, $month, $edit) = @_;
	local($day);
	local($days);
	local($firstwday);

	#対象データを取得
	&read_datafile($year, $month);
	
	#日数を取得
	$days = &get_days($year, $month);
	
	#最初の曜日を取得
	$firstwday = &get_wday($year, $month, 1);
	
	# 1段
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 1, $days);

	return $html;
}

#横長タイプ(上下2段)のカレンダーを取得
sub get_calender2
{
	local($html) = '';
	local($year, $month, $edit) = @_;
	local($days);
	local($firstwday);

	#対象データを取得
	&read_datafile($year, $month);
	
	#日数を取得
	$days = &get_days($year, $month);
	
	#最初の曜日を取得
	$firstwday = &get_wday($year, $month, 1);
	
	# 1段目
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 1, 16);
	$html .= "<br>";

	# 2段目
	$html .= &get_calender_row($year, $month, $edit, $firstwday, 17, $days);

	return $html;
}

# 横長カレンダーの1段分
sub get_calender_row
{
	local($year, $month, $edit, $firstwday, $stday, $edday) = @_;
	local($html) = '';
	local($span);
	local($day);
	local($i, $j, $k);
	local($calwidth);
	local($holiday);

	#カレンダー幅を計算(実際にこのテーブルに含まれる日数に基づいた計算)
	$calwidth = ($edday - $stday + 1) * $colwidth_day + $colwidth_rowtitle;

	#微調整
	$calwidth = $calwidth 
			+ ($edday - $stday + 2) * 1 * 2	# セル数 * 1dot * 左右
			+ ($edday - $stday + 3) * 2;	# 本数 * 2dot

	#年月日のrowspanを計算
	if ($showpname) {
		$span = 2;
	} else {
		$span = 2 + $periods;
	}

	#テーブル開始
	$html =<<"EOM";
<table border=1 cellspacing=0 width="$calwidth">
<tr><td rowspan=$span align="center" bgcolor="$caltitle_color" width="$colwidth_rowtitle">$year年$month月</td>
EOM

	#日付
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

	#曜日名
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

	#状態枠ごとにHTML作成
	for ($i = 0; $i < $periods; $i++) {
		$html .= "<tr>\n";

		#状態枠名
		if ($showpname) {
			$html .= "<td width=\"$colwidth_rowtitle\">$periodname[$i]</td>\n";
		}

		#日ごとにHTML作成
		for ($j = $stday; $j <= $edday; $j++) {
			$day = $j;
			@stats = split(/;/, $STATUS[$day]);

			#編集モード以外は表示するだけ、編集モード時はコンボボックスで表示
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

	#テーブル終了
	$html .= "</table>\n";

	return $html;
}

#対象データを取得
sub read_datafile
{
	local($year, $month) = @_;
	local($y, $m, $d, $stat);
	local($i);
	
	#今日以降の初期値を作成
	local($default_stat_1day) = '';
	
	for ($i = 0; $i < $periods; $i++) {
		$default_stat_1day .= $default_stat;
		$default_stat_1day .= ';';
	}

    #現在日を取得
    $ENV{'TZ'} = "JST-9";
    local($sec,$min,$hour,$nd,$nm,$ny) = localtime(time);
    $ny = 1900 + $ny;
    $nm++;

	#データを初期化
	for ($i = 1; $i < 32; $i++) {
		$STATUS[$i] = 0;

        #今日以降のデータ未設定日は $default_stat にする
        if (($year*10000+$month*100+$i) >= ($ny*10000+$nm*100+$nd)) {
            $STATUS[$i] = $default_stat_1day;
        }
	}
	
	#ファイルを開く
	open(IN, $datafile);

	while (<IN>) {
		#デコード
		($y, $m, $d, $stat) = split(/<>/,$_);

		#該当データを設定
		if (($y == $year) && ($m == $month)) {
			$STATUS[$d] = $stat;
		}
	}

	close(IN);
}

################################################################################
#
#	予約表示(SSIバージョン)
#
################################################################################

#予約表示
sub ssishow
{
	local($html);
	local($calender);
	
	#古いデータを削除
	&delete_old_data;
	
	#対象年月を取得
	local($year, $month) = &get_target_month();

	#前後の月を取得
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
	
	#状態文字列を取得
	&read_strfile;
	
	#祝日を取得
	&read_holiday($year, $month);

	#カレンダー表示部を取得
	$calender = &get_calender($year, $month, 0);
	
	#HTML作成
	$html = $calender;

	#表示
	&print_html($html);
}

################################################################################
#
#	予約編集
#
################################################################################

#予約編集
sub edit
{
	local($html);
	local($calender);
	local($copyright);

	#パスワードチェック
	if ($FORM{'pwd'} ne $pwd) {
		&error("パスワードが違います。");
		return;
	}
	
	#対象年月を取得
	local($year, $month) = &get_target_month();

	#状態文字列を取得
	&read_strfile;
	
	#祝日を取得
	&read_holiday($year, $month);

	#カレンダー表示部を取得
	$calender = &get_calender($year, $month, 1);
	
	#著作権表示部を取得
	$copyright = &get_copyright;

	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>$year年$month月の予約状況:編集モード</title>
</head>
<body bgcolor="$bgcolor">
<form action="$self" method=post>
<input type=hidden name=mode value="save">
<input type=hidden name=month value="$year/$month">
<input type=hidden name=pwd value="$FORM{'pwd'}">

<p><a href="$self?mode=mng&pwd=$FORM{'pwd'}">戻る</a></p>
<b>予約状況一覧:編集モード</b>
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
<input type=submit value="　登録する　">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#表示
	&print_html($html);
}

################################################################################
#
#	予約保存
#
################################################################################

#予約保存
sub save
{
	local($html);
	local(@lines);
	
	#パスワードチェック
	if ($FORM{'pwd'} ne $pwd) {
		&error("パスワードが違います。");
		return;
	}

	#対象年月を取得
	local($year, $month) = &get_target_month();

	#日数を取得
	local($days) = &get_days($year, $month);
	
	#日数分のデータを書き込み可能な書式に変換
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

	#ロック
	if (!&lock($lockdir)) {
		&error("ロック処理に失敗しました。");
		return;
	}
	
	#現在のデータを読み込む(更新対象のデータは除く)
	local($y, $m, $d, $stat);
	
	open(IN, $datafile);

	while (<IN>) {
		#デコード
		($y, $m, $d, $stat) = split(/<>/, $_);

		#該当データを設定
		if (($y != $year) || ($m != $month)) {
			push(@lines, $_);
		}
	}

	close(IN);
	
	#ファイルを更新
	open(OUT, ">$datafile");
	print OUT @lines;
	close(OUT);
	
	#更新日記録ファイルを更新
	open(OUT, ">$updfile");
	print OUT "dummy text";
	close(OUT);

	#ロック解除
	&unlock($lockdir);
	
	#管理画面に戻る
	&mng;
}

################################################################################
#
#	文字列の編集
#
################################################################################

#文字列の編集
sub editstr
{
	local($html);
	local($copyright);

	#パスワードチェック
	if ($FORM{'pwd'} ne $pwd) {
		&error("パスワードが違います。");
		return;
	}
	
	#状態文字列を取得
	&read_strfile;

	#著作権表示部を取得
	$copyright = &get_copyright;

	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>状態文字列の編集</title>
</head>
<body bgcolor="$bgcolor">
<form action="$self" method=post>
<input type=hidden name=mode value="savestr">
<input type=hidden name=pwd value="$FORM{'pwd'}">

<p><a href="$self?mode=mng&pwd=$FORM{'pwd'}">戻る</a></p>
<b>状態文字列の編集</b>
<hr>
<table border=0>

<tr><td><b>状況</b></td><td><b>記号</b></td><td><b>状況を説明する文字</b></td></tr>

<tr><td>空きがあるとき</td>
<td><input type=text name=str1 value="$STATUSSTR[1]" size=10></td>
<td><input type=text name=strl1 value="$STATUSSTRL[1]" size=30></td></tr>

<tr><td>空きが少ないとき</td>
<td><input type=text name=str2 value="$STATUSSTR[2]" size=10></td>
<td><input type=text name=strl2 value="$STATUSSTRL[2]" size=30></td></tr>

<tr><td>空きがないとき</td>
<td><input type=text name=str3 value="$STATUSSTR[3]" size=10></td>
<td><input type=text name=strl3 value="$STATUSSTRL[3]" size=30></td></tr>

<tr><td>未設定</td>
<td><input type=text name=str0 value="$STATUSSTR[0]" size=10></td>
<td><input type=text name=strl0 value="$STATUSSTRL[0]" size=30></td></tr>

<tr><td>要問い合わせ</td>
<td><input type=text name=str4 value="$STATUSSTR[4]" size=10></td>
<td><input type=text name=strl4 value="$STATUSSTRL[4]" size=30></td></tr>

</table>
<br>
<input type=submit value="　登録する　">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#表示
	&print_html($html);
}

################################################################################
#
#	文字列の編集を保存
#
################################################################################

#文字列の編集を保存
sub savestr
{
	#パスワードチェック
	if ($FORM{'pwd'} ne $pwd) {
		&error("パスワードが違います。");
		return;
	}
	
	#新しいデータを作成
	local(@lines);
	
	push(@lines, "0<>$FORM{'str0'}<>$FORM{'strl0'}<>\n");
	push(@lines, "1<>$FORM{'str1'}<>$FORM{'strl1'}<>\n");
	push(@lines, "2<>$FORM{'str2'}<>$FORM{'strl2'}<>\n");
	push(@lines, "3<>$FORM{'str3'}<>$FORM{'strl3'}<>\n");
	push(@lines, "4<>$FORM{'str4'}<>$FORM{'strl4'}<>\n");
	

	#ロック
	if (!&lock($lockdir)) {
		&error("ロック処理に失敗しました。");
		return;
	}
	
	#ファイルを更新
	open(OUT, ">$strfile");
	print OUT @lines;
	close(OUT);
	
	#ロック解除
	&unlock($lockdir);
	
	#管理画面に戻る
	&mng;
}

################################################################################
#
#	管理画面
#
################################################################################

#管理画面
sub mng
{
	local($html);
	local($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst);
	local($copyright);

	#パスワードが指定されていない場合はパスワード入力画面を表示
	if ($FORM{'pwd'} eq '') {
		&pwd_input;
		return;
	}

	#パスワードチェック
	if ($FORM{'pwd'} ne $pwd) {
		&error("パスワードが違います。");
		return;
	}
	
	#現在の日時を取得
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime(time);
	$year = 1900 + $year;
	$month++;

	#著作権表示部を取得
	$copyright = &get_copyright;

	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>予約状況管理画面</title>
</head>
<body bgcolor="$bgcolor">
<p><a href="$home">戻る</a></p>
<b>予約状況管理画面</b>
<hr>
<p>■ 予約状況の編集</p>
<form action="$self" method=post>
<input type=hidden name=mode value="edit">
<input type=hidden name=pwd value=$FORM{'pwd'}>
年/月：　<input type=text name=month value="$year/$month" size=10>
　
<input type=radio name="disptype" value="0" checked>標準　
<input type=radio name="disptype" value="1">横長1段　
<input type=radio name="disptype" value="2">横長2段<br><br>
<input type=submit value="編集">
</form>
<p>■ 予約状況文字の編集</p>
<form action="$self" method=post>
<input type=hidden name=mode value="editstr">
<input type=hidden name=pwd value=$FORM{'pwd'}>
<input type=submit value="編集">
</form>
<br>
$copyright
<hr>
</body>
</html>
EOM

	#表示
	&print_html($html);
}

#パスワード入力画面
sub pwd_input
{
	local($html) = '';
	
	#HTML作成
	$html = << "EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=$charset">
<title>パスワード入力</title>
</head>
<body text="#333333" bgcolor="#ffffff">
<br>
<hr>
<form action="$self" method=post>
パスワード：<input type=password name=pwd>
<input type=submit value="管理画面">
</form>
<hr>
</body>
</html>
EOM

	#表示
	&print_html($html);
}

################################################################################
#
#	更新日の取得
#
################################################################################

#更新日時をSSIで表示
sub updtime
{
	local($html);
	local($updtime);
	
	#ファイルの更新日を取得
	$updtime = &get_upddate($updfile);
	
	#HTML作成
	$html = $updtime;

	#表示
	&print_html($html);
}

#ファイルの更新日を取得
sub get_upddate
{
	local($file) = @_;
	local($updtime) = $updtime_format;
	local($tmp);
	
	#呼び出し時に書式指定があればそれを優先
	if ($FORM{'fmt'} ne '') {
		$updtime = $FORM{'fmt'};
	}
	
	#ファイルの更新日を取得
	local($mtime) = (stat($file))[9];
	local($s,$m,$h,$day,$mon,$year) = localtime($mtime);

	#localtimeの値を調整
	$year = 1900 + $year;
	$mon++;
	
	#年(YYYY)
	$updtime =~ s/YYYY/$year/;
	
	#年(YY)
	$tmp = sprintf("%02d", $year % 100);
	$updtime =~ s/YY/$tmp/;
	
	#月(MM)
	$tmp = sprintf("%02d", $mon);
	$updtime =~ s/MM/$tmp/;
	
	#月(M)
	$updtime =~ s/M/$mon/;
	
	#日(DD)
	$tmp = sprintf("%02d", $day);
	$updtime =~ s/DD/$tmp/;
	
	#日(D)
	$updtime =~ s/D/$day/;
	
	#時(hh)
	$tmp = sprintf("%02d", $h);
	$updtime =~ s/hh/$tmp/;
	
	#時(h)
	$updtime =~ s/h/$h/;

	#分(mm)
	$tmp = sprintf("%02d", $m);
	$updtime =~ s/mm/$tmp/;
	
	#分(m)
	$updtime =~ s/m/$m/;

	#秒(ss)
	$tmp = sprintf("%02d", $s);
	$updtime =~ s/ss/$tmp/;
	
	#秒(s)
	$updtime =~ s/s/$s/;

	return $updtime;
}

################################################################################
#
#	著作権表示の取得
#
################################################################################

#著作権表示の取得
sub get_copyright
{
	#著作権
	local($copyright) = << "EOM";
<table border=0 width="$calwidth"><tr><td align="center">
- <a href="http://www.dab.hi-ho.ne.jp/appletea/cgikan/" 
target="_blank">CGI提供:CGIのかんづめ</a> -
</td></tr></table>
EOM

	return $copyright;
}

################################################################################
