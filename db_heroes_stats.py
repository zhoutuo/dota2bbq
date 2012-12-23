import re
import sqlite3
data = """
<!DOCTYPE html>
<html lang="en" dir="ltr" class="client-nojs">
<head>
<title>Table of Hero attributes - Dota 2 Wiki</title>
<meta charset="UTF-8" />
<meta name="generator" content="MediaWiki 1.18.6" />
<link rel="stylesheet" href="/extensions/CommunityVoice/Resources/CommunityVoice.css" />
<link rel="alternate" type="application/x-wiki" title="Edit" href="/index.php?title=Table_of_Hero_attributes&amp;action=edit" />
<link rel="edit" title="Edit" href="/index.php?title=Table_of_Hero_attributes&amp;action=edit" />
<link rel="shortcut icon" href="/images/custom_images/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="Dota 2 Wiki (en)" />
<link rel="EditURI" type="application/rsd+xml" href="http://www.dota2wiki.com/api.php?action=rsd" />
<link rel="copyright" href="/wiki/Dota_2_Wiki" />
<link rel="alternate" type="application/atom+xml" title="Dota 2 Wiki Atom feed" href="/index.php?title=Special:RecentChanges&amp;feed=atom" />
<link rel="stylesheet" href="/load.php?debug=false&amp;lang=en&amp;modules=mediawiki.legacy.commonPrint%2Cshared%7Cskins.vector&amp;only=styles&amp;skin=vector&amp;*" />
<meta name="ResourceLoaderDynamicStyles" content="" />
<link rel="stylesheet" href="/load.php?debug=false&amp;lang=en&amp;modules=site&amp;only=styles&amp;skin=vector&amp;*" />
<style>a:lang(ar),a:lang(ckb),a:lang(fa),a:lang(kk-arab),a:lang(mzn),a:lang(ps),a:lang(ur){text-decoration:none}a.new,#quickbar a.new{color:#ba0000}

/* cache key: dota2wiki-dotawiki_:resourceloader:filter:minify-css:4:c88e2bcd56513749bec09a7e29cb3ffa */</style>
<script src="/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
	mw.config.set({"wgCanonicalNamespace": "", "wgCanonicalSpecialPageName": false, "wgNamespaceNumber": 0, "wgPageName": "Table_of_Hero_attributes", "wgTitle": "Table of Hero attributes", "wgCurRevisionId": 149867, "wgArticleId": 27839, "wgIsArticle": true, "wgAction": "view", "wgUserName": null, "wgUserGroups": ["*"], "wgCategories": [], "wgBreakFrames": false, "wgRestrictionEdit": [], "wgRestrictionMove": [], "wgSearchNamespaces": [0], "wgWikiEditorEnabledModules": {"toolbar": true, "dialogs": true, "hidesig": true, "templateEditor": false, "templates": false, "preview": false, "previewDialog": false, "publish": false, "toc": false}});
}
</script><script>if(window.mw){
	mw.loader.load(["mediawiki.page.startup"]);
}
</script>
		<link rel="alternate" type="application/rdf+xml" title="Table of Hero attributes" href="/index.php?title=Special:ExportRDF/Table_of_Hero_attributes&amp;xmlmime=rdf" />
<!--[if lt IE 7]><style type="text/css">body{behavior:url("/skins/vector/csshover.min.htc")}</style><![endif]--></head>
<body class="mediawiki ltr sitedir-ltr ns-0 ns-subject page-Table_of_Hero_attributes action-view skin-vector site-dota2wiki">
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<!-- content -->
		<div id="content">
			<a id="top"></a>
			<div id="mw-js-message" style="display:none;"></div>
			
            <div style="text-align: center; padding: 5px; width: 1200px; margin: 0 auto;" class="atflb">
                <!-- Begin Advertising // Tag for network 5259: Curse.com // Website: dota2wiki // Page: Default // Placement: Dota2wiki_Default_Above_728x90 (2226915) // created at: Nov 3, 2011 2:31:01 PM -->
                <script language="javascript">
                    <!--
                    if (window.adgroupid == undefined) {
                        window.adgroupid = Math.round(Math.random() * 1000);
                    }
                    document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtechus.com/addyn/3.0/5259.1/2226915/0/225/ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
                    //-->
                </script><noscript><a href="http://adserver.adtechus.com/adlink/3.0/5259.1/2226915/0/225/ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtechus.com/adserv/3.0/5259.1/2226915/0/225/ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
                <!-- End Advertising -->
            </div>

			<!-- firstHeading -->
			<h1 id="firstHeading" class="firstHeading">Table of Hero attributes</h1>
			<!-- /firstHeading -->
			<!-- bodyContent -->
							<div id="bodyContent2" class="en">
											<!-- tagline -->
				<div id="siteSub">From Dota 2 Wiki</div>
				<!-- /tagline -->
								<!-- subtitle -->
				<div id="contentSub"></div>
				<!-- /subtitle -->
																<!-- jumpto -->
				<div id="jump-to-nav">
					Jump to: <a href="#mw-head">navigation</a>,
					<a href="#p-search">search</a>
				</div>
				<!-- /jumpto -->
								<!-- bodycontent -->
				<div lang="en" dir="ltr" class="mw-content-ltr"><table class="wikitable sortable" width="100%">
<tr>
<th class="unsortable" width="100px">
</th>
<th> Hero
</th>
<th> Base Str
</th>
<th> Str Growth
</th>
<th> Base Agi
</th>
<th> Agi Growth
</th>
<th> Base Int
</th>
<th> Int Growth
</th>
<th> Movement speed
</th>
<th> Starting Armor
</th>
<th> BAT
</th>
<th> Damage (min)
</th>
<th> Damage (max)
</th>
<th> Attack range
</th>
<th> Missile speed
</th>
<th> Attack point
</th>
<th> Cast point
</th>
<th> Day sight range
</th>
<th> Night sight range
</th></tr>
<tr>
<td><a href="/wiki/Alchemist" title="Alchemist"><img alt="Alchemist.png" src="/images/thumb/5/5b/Alchemist.png/100px-Alchemist.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Alchemist" title="Alchemist">Alchemist</a>
</td>
<td align="center"> 25
</td>
<td align="center"> 1.8
</td>
<td align="center"> 11
</td>
<td align="center"> 1.2
</td>
<td align="center"> 25
</td>
<td align="center"> 1.8
</td>
<td align="center"> 295
</td>
<td align="center"> 1.54
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 58
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.35
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 1400
</td></tr>

<tr>
<td><a href="/wiki/Ancient_Apparition" title="Ancient Apparition"><img alt="Ancient Apparition.png" src="/images/thumb/b/b1/Ancient_Apparition.png/100px-Ancient_Apparition.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Ancient_Apparition" title="Ancient Apparition">Ancient Apparition</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.4
</td>
<td align="center"> 20
</td>
<td align="center"> 2.2
</td>
<td align="center"> 25
</td>
<td align="center"> 2.6
</td>
<td align="center"> 295
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 54
</td>
<td align="center"> 600
</td>
<td align="center"> 1250
</td>
<td align="center"> 0.45
</td>
<td align="center"> 0.01
</td>
<td align="center"> 1800
</td>
<td align="center"> 1400
</td></tr>

<tr>
<td><a href="/wiki/Anti-Mage" title="Anti-Mage"><img alt="Anti-Mage.png" src="/images/thumb/e/ef/Anti-Mage.png/100px-Anti-Mage.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Anti-Mage" title="Anti-Mage">Anti-Mage</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 1.2
</td>
<td align="center"> 22
</td>
<td align="center"> 2.8
</td>
<td align="center"> 15
</td>
<td align="center"> 1.8
</td>
<td align="center"> 315
</td>
<td align="center"> 2.08
</td>
<td align="center"> 1.45
</td>
<td align="center"> 49
</td>
<td align="center"> 53
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Axe" title="Axe"><img alt="Axe.png" src="/images/thumb/f/fb/Axe.png/100px-Axe.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Axe" title="Axe">Axe</a>
</td>
<td align="center"> 25
</td>
<td align="center"> 2.5
</td>
<td align="center"> 20
</td>
<td align="center"> 2.2
</td>
<td align="center"> 18
</td>
<td align="center"> 1.6
</td>
<td align="center"> 290
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 53
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Bane" title="Bane"><img alt="Bane.png" src="/images/thumb/9/9a/Bane.png/100px-Bane.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Bane" title="Bane">Bane</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.1
</td>
<td align="center"> 22
</td>
<td align="center"> 2.1
</td>
<td align="center"> 22
</td>
<td align="center"> 2.1
</td>
<td align="center"> 315
</td>
<td align="center"> 3.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 51
</td>
<td align="center"> 57
</td>
<td align="center"> 400
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Batrider" title="Batrider"><img alt="Batrider.png" src="/images/thumb/5/5e/Batrider.png/100px-Batrider.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Batrider" title="Batrider">Batrider</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.4
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 24
</td>
<td align="center"> 2.5
</td>
<td align="center"> 290
</td>
<td align="center"> 2.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 52
</td>
<td align="center"> 375
</td>
<td align="center"> 900
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.2
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Beastmaster" title="Beastmaster"><img alt="Beastmaster.png" src="/images/thumb/d/d6/Beastmaster.png/100px-Beastmaster.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Beastmaster" title="Beastmaster">Beastmaster</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2.2
</td>
<td align="center"> 18
</td>
<td align="center"> 1.6
</td>
<td align="center"> 16
</td>
<td align="center"> 1.9
</td>
<td align="center"> 310
</td>
<td align="center"> 4.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 56
</td>
<td align="center"> 60
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Bloodseeker" title="Bloodseeker"><img alt="Bloodseeker.png" src="/images/thumb/1/1e/Bloodseeker.png/100px-Bloodseeker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Bloodseeker" title="Bloodseeker">Bloodseeker</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2
</td>
<td align="center"> 24
</td>
<td align="center"> 3
</td>
<td align="center"> 18
</td>
<td align="center"> 1.7
</td>
<td align="center"> 305
</td>
<td align="center"> 3.36
</td>
<td align="center"> 1.7
</td>
<td align="center"> 53
</td>
<td align="center"> 59
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.43
</td>
<td align="center"> 0.6
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Bounty_Hunter" title="Bounty Hunter"><img alt="Bounty Hunter.png" src="/images/thumb/1/1d/Bounty_Hunter.png/100px-Bounty_Hunter.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Bounty_Hunter" title="Bounty Hunter">Bounty Hunter</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.8
</td>
<td align="center"> 21
</td>
<td align="center"> 3
</td>
<td align="center"> 19
</td>
<td align="center"> 1.4
</td>
<td align="center"> 315
</td>
<td align="center"> 5.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 59
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.6
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 1000
</td></tr>

<tr>
<td><a href="/wiki/Brewmaster" title="Brewmaster"><img alt="Brewmaster.png" src="/images/thumb/4/43/Brewmaster.png/100px-Brewmaster.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Brewmaster" title="Brewmaster">Brewmaster</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2.9
</td>
<td align="center"> 16
</td>
<td align="center"> 1.95
</td>
<td align="center"> 14
</td>
<td align="center"> 1.25
</td>
<td align="center"> 300
</td>
<td align="center"> 3.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 52
</td>
<td align="center"> 59
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.35
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Broodmother" title="Broodmother"><img alt="Broodmother.png" src="/images/thumb/1/19/Broodmother.png/100px-Broodmother.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Broodmother" title="Broodmother">Broodmother</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2.5
</td>
<td align="center"> 18
</td>
<td align="center"> 2.2
</td>
<td align="center"> 18
</td>
<td align="center"> 2
</td>
<td align="center"> 295
</td>
<td align="center"> 2.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 50
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.2
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Centaur_Warrunner" title="Centaur Warrunner"><img alt="Centaur Warrunner.png" src="/images/thumb/b/b6/Centaur_Warrunner.png/100px-Centaur_Warrunner.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Centaur_Warrunner" title="Centaur Warrunner">Centaur Warrunner</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 3.8
</td>
<td align="center"> 15
</td>
<td align="center"> 2
</td>
<td align="center"> 15
</td>
<td align="center"> 1.6
</td>
<td align="center"> 300
</td>
<td align="center"> 3.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 55
</td>
<td align="center"> 57
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Chaos_Knight" title="Chaos Knight"><img alt="Chaos Knight.png" src="/images/thumb/c/cf/Chaos_Knight.png/100px-Chaos_Knight.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Chaos_Knight" title="Chaos Knight">Chaos Knight</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 2.9
</td>
<td align="center"> 14
</td>
<td align="center"> 2.1
</td>
<td align="center"> 16
</td>
<td align="center"> 1.2
</td>
<td align="center"> 325
</td>
<td align="center"> 3.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 79
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Chen" title="Chen"><img alt="Chen.png" src="/images/thumb/8/80/Chen.png/100px-Chen.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Chen" title="Chen">Chen</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 1.5
</td>
<td align="center"> 15
</td>
<td align="center"> 2.1
</td>
<td align="center"> 21
</td>
<td align="center"> 2.8
</td>
<td align="center"> 300
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 53
</td>
<td align="center"> 600
</td>
<td align="center"> 1100
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Clinkz" title="Clinkz"><img alt="Clinkz.png" src="/images/thumb/9/9c/Clinkz.png/100px-Clinkz.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Clinkz" title="Clinkz">Clinkz</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 1.6
</td>
<td align="center"> 22
</td>
<td align="center"> 3
</td>
<td align="center"> 16
</td>
<td align="center"> 1.55
</td>
<td align="center"> 300
</td>
<td align="center"> 2.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 37
</td>
<td align="center"> 43
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.7
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Clockwerk" title="Clockwerk"><img alt="Clockwerk.png" src="/images/thumb/b/b3/Clockwerk.png/100px-Clockwerk.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Clockwerk" title="Clockwerk">Clockwerk</a>
</td>
<td align="center"> 24
</td>
<td align="center"> 2.7
</td>
<td align="center"> 13
</td>
<td align="center"> 2.3
</td>
<td align="center"> 17
</td>
<td align="center"> 1.3
</td>
<td align="center"> 315
</td>
<td align="center"> 1.82
</td>
<td align="center"> 1.7
</td>
<td align="center"> 55
</td>
<td align="center"> 57
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.33
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Crystal_Maiden" title="Crystal Maiden"><img alt="Crystal Maiden.png" src="/images/thumb/1/10/Crystal_Maiden.png/100px-Crystal_Maiden.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Crystal_Maiden" title="Crystal Maiden">Crystal Maiden</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.7
</td>
<td align="center"> 16
</td>
<td align="center"> 1.6
</td>
<td align="center"> 21
</td>
<td align="center"> 2.9
</td>
<td align="center"> 280
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 38
</td>
<td align="center"> 44
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.55
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Dark_Seer" title="Dark Seer"><img alt="Dark Seer.png" src="/images/thumb/f/f7/Dark_Seer.png/100px-Dark_Seer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Dark_Seer" title="Dark Seer">Dark Seer</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.3
</td>
<td align="center"> 12
</td>
<td align="center"> 1.2
</td>
<td align="center"> 29
</td>
<td align="center"> 2.7
</td>
<td align="center"> 300
</td>
<td align="center"> 5.68
</td>
<td align="center"> 1.7
</td>
<td align="center"> 60
</td>
<td align="center"> 66
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.59
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Dazzle" title="Dazzle"><img alt="Dazzle.png" src="/images/thumb/7/74/Dazzle.png/100px-Dazzle.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Dazzle" title="Dazzle">Dazzle</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.85
</td>
<td align="center"> 21
</td>
<td align="center"> 1.7
</td>
<td align="center"> 27
</td>
<td align="center"> 3.4
</td>
<td align="center"> 305
</td>
<td align="center"> 1.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 41
</td>
<td align="center"> 59
</td>
<td align="center"> 500
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Death_Prophet" title="Death Prophet"><img alt="Death Prophet.png" src="/images/thumb/5/52/Death_Prophet.png/100px-Death_Prophet.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Death_Prophet" title="Death Prophet">Death Prophet</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 2.2
</td>
<td align="center"> 14
</td>
<td align="center"> 1.4
</td>
<td align="center"> 20
</td>
<td align="center"> 3
</td>
<td align="center"> 285
</td>
<td align="center"> 2.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 56
</td>
<td align="center"> 600
</td>
<td align="center"> 1000
</td>
<td align="center"> 0.56
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Disruptor" title="Disruptor"><img alt="Disruptor.png" src="/images/thumb/c/ce/Disruptor.png/100px-Disruptor.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Disruptor" title="Disruptor">Disruptor</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.9
</td>
<td align="center"> 15
</td>
<td align="center"> 1.4
</td>
<td align="center"> 22
</td>
<td align="center"> 2.5
</td>
<td align="center"> 300
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 53
</td>
<td align="center"> 600
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.05
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Doom_Bringer" title="Doom Bringer"><img alt="Doom Bringer.png" src="/images/thumb/a/a9/Doom_Bringer.png/100px-Doom_Bringer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Doom_Bringer" title="Doom Bringer">Doom Bringer</a>
</td>
<td align="center"> 26
</td>
<td align="center"> 3.2
</td>
<td align="center"> 11
</td>
<td align="center"> 0.9
</td>
<td align="center"> 13
</td>
<td align="center"> 2.1
</td>
<td align="center"> 290
</td>
<td align="center"> 0.54
</td>
<td align="center"> 1.7
</td>
<td align="center"> 53
</td>
<td align="center"> 69
</td>
<td align="center"> 150
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Dragon_Knight" title="Dragon Knight"><img alt="Dragon Knight.png" src="/images/thumb/4/4e/Dragon_Knight.png/100px-Dragon_Knight.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Dragon_Knight" title="Dragon Knight">Dragon Knight</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 2.8
</td>
<td align="center"> 19
</td>
<td align="center"> 2.2
</td>
<td align="center"> 15
</td>
<td align="center"> 1.7
</td>
<td align="center"> 290
</td>
<td align="center"> 3.66
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 52
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Drow_Ranger" title="Drow Ranger"><img alt="Drow Ranger.png" src="/images/thumb/3/36/Drow_Ranger.png/100px-Drow_Ranger.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Drow_Ranger" title="Drow Ranger">Drow Ranger</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.9
</td>
<td align="center"> 26
</td>
<td align="center"> 1.9
</td>
<td align="center"> 15
</td>
<td align="center"> 1.4
</td>
<td align="center"> 300
</td>
<td align="center"> 0.64
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 55
</td>
<td align="center"> 625
</td>
<td align="center"> 1250
</td>
<td align="center"> 0.7
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 1700
</td></tr>

<tr>
<td><a href="/wiki/Earthshaker" title="Earthshaker"><img alt="Earthshaker.png" src="/images/thumb/b/bd/Earthshaker.png/100px-Earthshaker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Earthshaker" title="Earthshaker">Earthshaker</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.5
</td>
<td align="center"> 12
</td>
<td align="center"> 1.4
</td>
<td align="center"> 16
</td>
<td align="center"> 1.8
</td>
<td align="center"> 300
</td>
<td align="center"> 2.68
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 56
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.467
</td>
<td align="center"> 0.69
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Enchantress" title="Enchantress"><img alt="Enchantress.png" src="/images/thumb/9/99/Enchantress.png/100px-Enchantress.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Enchantress" title="Enchantress">Enchantress</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1
</td>
<td align="center"> 19
</td>
<td align="center"> 1.8
</td>
<td align="center"> 16
</td>
<td align="center"> 2.8
</td>
<td align="center"> 310
</td>
<td align="center"> 1.66
</td>
<td align="center"> 1.7
</td>
<td align="center"> 47
</td>
<td align="center"> 57
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 1800
</td></tr>

<tr>
<td><a href="/wiki/Enigma" title="Enigma"><img alt="Enigma.png" src="/images/thumb/8/8b/Enigma.png/100px-Enigma.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Enigma" title="Enigma">Enigma</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2.1
</td>
<td align="center"> 14
</td>
<td align="center"> 1
</td>
<td align="center"> 20
</td>
<td align="center"> 3.4
</td>
<td align="center"> 300
</td>
<td align="center"> 3.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 42
</td>
<td align="center"> 48
</td>
<td align="center"> 500
</td>
<td align="center"> 900
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Faceless_Void" title="Faceless Void"><img alt="Faceless Void.png" src="/images/thumb/0/03/Faceless_Void.png/100px-Faceless_Void.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Faceless_Void" title="Faceless Void">Faceless Void</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 1.6
</td>
<td align="center"> 21
</td>
<td align="center"> 2.65
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 300
</td>
<td align="center"> 3.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 58
</td>
<td align="center"> 64
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.35
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Gyrocopter" title="Gyrocopter"><img alt="Gyrocopter.png" src="/images/thumb/5/5d/Gyrocopter.png/100px-Gyrocopter.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Gyrocopter" title="Gyrocopter">Gyrocopter</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.8
</td>
<td align="center"> 24
</td>
<td align="center"> 2.8
</td>
<td align="center"> 23
</td>
<td align="center"> 2.1
</td>
<td align="center"> 315
</td>
<td align="center"> 4.36
</td>
<td align="center"> 1.7
</td>
<td align="center"> 41
</td>
<td align="center"> 51
</td>
<td align="center"> 375
</td>
<td align="center"> 3000
</td>
<td align="center"> 0.2
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Huskar" title="Huskar"><img alt="Huskar.png" src="/images/thumb/2/2b/Huskar.png/100px-Huskar.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Huskar" title="Huskar">Huskar</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 2.4
</td>
<td align="center"> 20
</td>
<td align="center"> 2.4
</td>
<td align="center"> 18
</td>
<td align="center"> 1.5
</td>
<td align="center"> 300
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.6
</td>
<td align="center"> 39
</td>
<td align="center"> 48
</td>
<td align="center"> 400
</td>
<td align="center"> 1400
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Invoker" title="Invoker"><img alt="Invoker.png" src="/images/thumb/3/39/Invoker.png/100px-Invoker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Invoker" title="Invoker">Invoker</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.7
</td>
<td align="center"> 20
</td>
<td align="center"> 1.9
</td>
<td align="center"> 22
</td>
<td align="center"> 2.5
</td>
<td align="center"> 280
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.7
</td>
<td align="center"> 35
</td>
<td align="center"> 41
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Jakiro" title="Jakiro"><img alt="Jakiro.png" src="/images/thumb/1/1d/Jakiro.png/100px-Jakiro.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Jakiro" title="Jakiro">Jakiro</a>
</td>
<td align="center"> 24
</td>
<td align="center"> 2.3
</td>
<td align="center"> 10
</td>
<td align="center"> 1.2
</td>
<td align="center"> 28
</td>
<td align="center"> 2.8
</td>
<td align="center"> 290
</td>
<td align="center"> 2.4
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 54
</td>
<td align="center"> 400
</td>
<td align="center"> 1100
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.65
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Juggernaut" title="Juggernaut"><img alt="Juggernaut.png" src="/images/thumb/0/07/Juggernaut.png/100px-Juggernaut.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Juggernaut" title="Juggernaut">Juggernaut</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 1.9
</td>
<td align="center"> 20
</td>
<td align="center"> 2.85
</td>
<td align="center"> 14
</td>
<td align="center"> 1.4
</td>
<td align="center"> 305
</td>
<td align="center"> 3.8
</td>
<td align="center"> 1.6
</td>
<td align="center"> 44
</td>
<td align="center"> 48
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.33
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Keeper_of_the_Light" title="Keeper of the Light"><img alt="Keeper of the Light.png" src="/images/thumb/5/5c/Keeper_of_the_Light.png/100px-Keeper_of_the_Light.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Keeper_of_the_Light" title="Keeper of the Light">Keeper of the Light</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.8
</td>
<td align="center"> 15
</td>
<td align="center"> 1.6
</td>
<td align="center"> 22
</td>
<td align="center"> 2.8
</td>
<td align="center"> 315
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 38
</td>
<td align="center"> 54
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Kunkka" title="Kunkka"><img alt="Kunkka.png" src="/images/thumb/8/89/Kunkka.png/100px-Kunkka.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Kunkka" title="Kunkka">Kunkka</a>
</td>
<td align="center"> 24
</td>
<td align="center"> 3
</td>
<td align="center"> 14
</td>
<td align="center"> 1.3
</td>
<td align="center"> 18
</td>
<td align="center"> 1.5
</td>
<td align="center"> 300
</td>
<td align="center"> 1.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 47
</td>
<td align="center"> 57
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Leshrac" title="Leshrac"><img alt="Leshrac.png" src="/images/thumb/e/e9/Leshrac.png/100px-Leshrac.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Leshrac" title="Leshrac">Leshrac</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.5
</td>
<td align="center"> 23
</td>
<td align="center"> 1.7
</td>
<td align="center"> 26
</td>
<td align="center"> 3
</td>
<td align="center"> 315
</td>
<td align="center"> 3.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 49
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.7
</td>
<td align="center"> 1800
</td>
<td align="center"> 900
</td></tr>

<tr>
<td><a href="/wiki/Lich" title="Lich"><img alt="Lich.png" src="/images/thumb/8/86/Lich.png/100px-Lich.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lich" title="Lich">Lich</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.55
</td>
<td align="center"> 15
</td>
<td align="center"> 2
</td>
<td align="center"> 18
</td>
<td align="center"> 3.25
</td>
<td align="center"> 315
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 42
</td>
<td align="center"> 51
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.46
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Lifestealer" title="Lifestealer"><img alt="Lifestealer.png" src="/images/thumb/6/65/Lifestealer.png/100px-Lifestealer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lifestealer" title="Lifestealer">Lifestealer</a>
</td>
<td align="center"> 25
</td>
<td align="center"> 2.4
</td>
<td align="center"> 18
</td>
<td align="center"> 1.9
</td>
<td align="center"> 15
</td>
<td align="center"> 1.75
</td>
<td align="center"> 315
</td>
<td align="center"> 1.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 57
</td>
<td align="center"> 67
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.39
</td>
<td align="center"> 0.01
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Lina" title="Lina"><img alt="Lina.png" src="/images/thumb/e/ec/Lina.png/100px-Lina.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lina" title="Lina">Lina</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.5
</td>
<td align="center"> 16
</td>
<td align="center"> 1.5
</td>
<td align="center"> 27
</td>
<td align="center"> 3.2
</td>
<td align="center"> 295
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 40
</td>
<td align="center"> 58
</td>
<td align="center"> 625
</td>
<td align="center"> 900
</td>
<td align="center"> 0.75
</td>
<td align="center"> 0.45
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Lion" title="Lion"><img alt="Lion.png" src="/images/thumb/4/47/Lion.png/100px-Lion.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lion" title="Lion">Lion</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.7
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 22
</td>
<td align="center"> 3
</td>
<td align="center"> 290
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 42
</td>
<td align="center"> 48
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.43
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Lone_Druid" title="Lone Druid"><img alt="Lone Druid.png" src="/images/thumb/3/3d/Lone_Druid.png/100px-Lone_Druid.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lone_Druid" title="Lone Druid">Lone Druid</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2.1
</td>
<td align="center"> 24
</td>
<td align="center"> 2.7
</td>
<td align="center"> 13
</td>
<td align="center"> 1.4
</td>
<td align="center"> 315
</td>
<td align="center"> 3.36
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 50
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.33
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Luna" title="Luna"><img alt="Luna.png" src="/images/thumb/1/13/Luna.png/100px-Luna.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Luna" title="Luna">Luna</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 1.9
</td>
<td align="center"> 22
</td>
<td align="center"> 2.8
</td>
<td align="center"> 16
</td>
<td align="center"> 1.85
</td>
<td align="center"> 330
</td>
<td align="center"> 3.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 54
</td>
<td align="center"> 330
</td>
<td align="center"> 900
</td>
<td align="center"> 0.46
</td>
<td align="center"> 0.6
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Lycanthrope" title="Lycanthrope"><img alt="Lycanthrope.png" src="/images/thumb/c/c1/Lycanthrope.png/100px-Lycanthrope.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Lycanthrope" title="Lycanthrope">Lycanthrope</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.75
</td>
<td align="center"> 16
</td>
<td align="center"> 1.9
</td>
<td align="center"> 17
</td>
<td align="center"> 1.55
</td>
<td align="center"> 305
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 53
</td>
<td align="center"> 57
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.55
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Magnus" title="Magnus"><img alt="Magnus.png" src="/images/thumb/5/58/Magnus.png/100px-Magnus.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Magnus" title="Magnus">Magnus</a>
</td>
<td align="center"> 21
</td>
<td align="center"> 2.75
</td>
<td align="center"> 15
</td>
<td align="center"> 2.5
</td>
<td align="center"> 17
</td>
<td align="center"> 1.65
</td>
<td align="center"> 315
</td>
<td align="center"> 4.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 61
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Meepo" title="Meepo"><img alt="Meepo.png" src="/images/thumb/0/03/Meepo.png/100px-Meepo.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Meepo" title="Meepo">Meepo</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 1.6
</td>
<td align="center"> 23
</td>
<td align="center"> 1.9
</td>
<td align="center"> 20
</td>
<td align="center"> 1.6
</td>
<td align="center"> 305
</td>
<td align="center"> 5.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 39
</td>
<td align="center"> 45
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.38
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 1800
</td></tr>

<tr>
<td><a href="/wiki/Mirana" title="Mirana"><img alt="Mirana.png" src="/images/thumb/f/f9/Mirana.png/100px-Mirana.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Mirana" title="Mirana">Mirana</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.85
</td>
<td align="center"> 20
</td>
<td align="center"> 2.75
</td>
<td align="center"> 17
</td>
<td align="center"> 1.65
</td>
<td align="center"> 300
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.7
</td>
<td align="center"> 38
</td>
<td align="center"> 49
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 1200
</td></tr>

<tr>
<td><a href="/wiki/Morphling" title="Morphling"><img alt="Morphling.png" src="/images/thumb/7/7f/Morphling.png/100px-Morphling.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Morphling" title="Morphling">Morphling</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 2
</td>
<td align="center"> 24
</td>
<td align="center"> 3
</td>
<td align="center"> 17
</td>
<td align="center"> 1.5
</td>
<td align="center"> 285
</td>
<td align="center"> 0.66
</td>
<td align="center"> 1.7
</td>
<td align="center"> 32
</td>
<td align="center"> 41
</td>
<td align="center"> 350
</td>
<td align="center"> 1300
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.25
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Naga_Siren" title="Naga Siren"><img alt="Naga Siren.png" src="/images/thumb/d/d5/Naga_Siren.png/100px-Naga_Siren.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Naga_Siren" title="Naga Siren">Naga Siren</a>
</td>
<td align="center"> 21
</td>
<td align="center"> 2.3
</td>
<td align="center"> 21
</td>
<td align="center"> 2.75
</td>
<td align="center"> 18
</td>
<td align="center"> 1.95
</td>
<td align="center"> 320
</td>
<td align="center"> 5.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 46
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.65
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Nature%27s_Prophet" title="Nature&#39;s Prophet"><img alt="Nature&#39;s Prophet.png" src="/images/thumb/a/aa/Nature%27s_Prophet.png/100px-Nature%27s_Prophet.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Nature%27s_Prophet" title="Nature's Prophet">Nature's Prophet</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.8
</td>
<td align="center"> 18
</td>
<td align="center"> 1.9
</td>
<td align="center"> 21
</td>
<td align="center"> 2.9
</td>
<td align="center"> 295
</td>
<td align="center"> 3.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 59
</td>
<td align="center"> 600
</td>
<td align="center"> 1125
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Necrolyte" title="Necrolyte"><img alt="Necrolyte.png" src="/images/thumb/7/7d/Necrolyte.png/100px-Necrolyte.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Necrolyte" title="Necrolyte">Necrolyte</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 2
</td>
<td align="center"> 15
</td>
<td align="center"> 1.7
</td>
<td align="center"> 22
</td>
<td align="center"> 2.5
</td>
<td align="center"> 290
</td>
<td align="center"> 3.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 49
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.7
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Night_Stalker" title="Night Stalker"><img alt="Night Stalker.png" src="/images/thumb/b/bb/Night_Stalker.png/100px-Night_Stalker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Night_Stalker" title="Night Stalker">Night Stalker</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2.8
</td>
<td align="center"> 18
</td>
<td align="center"> 2.25
</td>
<td align="center"> 16
</td>
<td align="center"> 1.6
</td>
<td align="center"> 295
</td>
<td align="center"> 5.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 57
</td>
<td align="center"> 61
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.55
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1200
</td>
<td align="center"> 1800
</td></tr>

<tr>
<td><a href="/wiki/Nyx_Assassin" title="Nyx Assassin"><img alt="Nyx Assassin.png" src="/images/thumb/9/9e/Nyx_Assassin.png/100px-Nyx_Assassin.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Nyx_Assassin" title="Nyx Assassin">Nyx Assassin</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 2
</td>
<td align="center"> 19
</td>
<td align="center"> 2.2
</td>
<td align="center"> 18
</td>
<td align="center"> 2.1
</td>
<td align="center"> 300
</td>
<td align="center"> 3.66
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 53
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.46
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Ogre_Magi" title="Ogre Magi"><img alt="Ogre Magi.png" src="/images/thumb/a/ae/Ogre_Magi.png/100px-Ogre_Magi.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Ogre_Magi" title="Ogre Magi">Ogre Magi</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 3.2
</td>
<td align="center"> 14
</td>
<td align="center"> 1.55
</td>
<td align="center"> 17
</td>
<td align="center"> 2.4
</td>
<td align="center"> 295
</td>
<td align="center"> 5.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 58
</td>
<td align="center"> 64
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.56
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Omniknight" title="Omniknight"><img alt="Omniknight.png" src="/images/thumb/a/ab/Omniknight.png/100px-Omniknight.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Omniknight" title="Omniknight">Omniknight</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 2.65
</td>
<td align="center"> 15
</td>
<td align="center"> 1.75
</td>
<td align="center"> 17
</td>
<td align="center"> 1.8
</td>
<td align="center"> 305
</td>
<td align="center"> 4.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 51
</td>
<td align="center"> 61
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.433
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Outworld_Destroyer" title="Outworld Destroyer"><img alt="Outworld Destroyer.png" src="/images/thumb/8/86/Outworld_Destroyer.png/100px-Outworld_Destroyer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Outworld_Destroyer" title="Outworld Destroyer">Outworld Destroyer</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.85
</td>
<td align="center"> 24
</td>
<td align="center"> 2
</td>
<td align="center"> 26
</td>
<td align="center"> 3.3
</td>
<td align="center"> 310
</td>
<td align="center"> 5.36
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 64
</td>
<td align="center"> 450
</td>
<td align="center"> 900
</td>
<td align="center"> 0.46
</td>
<td align="center"> 0.25
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Phantom_Assassin" title="Phantom Assassin"><img alt="Phantom Assassin.png" src="/images/thumb/f/f0/Phantom_Assassin.png/100px-Phantom_Assassin.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Phantom_Assassin" title="Phantom Assassin">Phantom Assassin</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 1.85
</td>
<td align="center"> 23
</td>
<td align="center"> 3.15
</td>
<td align="center"> 13
</td>
<td align="center"> 1
</td>
<td align="center"> 310
</td>
<td align="center"> 4.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 48
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Phantom_Lancer" title="Phantom Lancer"><img alt="Phantom Lancer.png" src="/images/thumb/5/51/Phantom_Lancer.png/100px-Phantom_Lancer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Phantom_Lancer" title="Phantom Lancer">Phantom Lancer</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.7
</td>
<td align="center"> 23
</td>
<td align="center"> 4.2
</td>
<td align="center"> 21
</td>
<td align="center"> 2
</td>
<td align="center"> 290
</td>
<td align="center"> 3.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 67
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Puck" title="Puck"><img alt="Puck.png" src="/images/thumb/b/b6/Puck.png/100px-Puck.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Puck" title="Puck">Puck</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 1.7
</td>
<td align="center"> 22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 24
</td>
<td align="center"> 2.4
</td>
<td align="center"> 295
</td>
<td align="center"> 2.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 47
</td>
<td align="center"> 58
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.1
</td>
<td align="center"> 1800
</td>
<td align="center"> 1200
</td></tr>

<tr>
<td><a href="/wiki/Pudge" title="Pudge"><img alt="Pudge.png" src="/images/thumb/9/9f/Pudge.png/100px-Pudge.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Pudge" title="Pudge">Pudge</a>
</td>
<td align="center"> 25
</td>
<td align="center"> 3.2
</td>
<td align="center"> 14
</td>
<td align="center"> 1.5
</td>
<td align="center"> 14
</td>
<td align="center"> 1.5
</td>
<td align="center"> 285
</td>
<td align="center"> 0.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 52
</td>
<td align="center"> 58
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Pugna" title="Pugna"><img alt="Pugna.png" src="/images/thumb/1/1a/Pugna.png/100px-Pugna.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Pugna" title="Pugna">Pugna</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.2
</td>
<td align="center"> 16
</td>
<td align="center"> 1
</td>
<td align="center"> 26
</td>
<td align="center"> 4
</td>
<td align="center"> 320
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 53
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.2
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Queen_of_Pain" title="Queen of Pain"><img alt="Queen of Pain.png" src="/images/thumb/b/b5/Queen_of_Pain.png/100px-Queen_of_Pain.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Queen_of_Pain" title="Queen of Pain">Queen of Pain</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.7
</td>
<td align="center"> 18
</td>
<td align="center"> 2
</td>
<td align="center"> 24
</td>
<td align="center"> 2.5
</td>
<td align="center"> 300
</td>
<td align="center"> 1.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 57
</td>
<td align="center"> 550
</td>
<td align="center"> 1500
</td>
<td align="center"> 0.56
</td>
<td align="center"> 0.452
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Razor" title="Razor"><img alt="Razor.png" src="/images/thumb/a/a0/Razor.png/100px-Razor.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Razor" title="Razor">Razor</a>
</td>
<td align="center"> 21
</td>
<td align="center"> 1.7
</td>
<td align="center"> 22
</td>
<td align="center"> 2
</td>
<td align="center"> 19
</td>
<td align="center"> 1.8
</td>
<td align="center"> 295
</td>
<td align="center"> 2.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 47
</td>
<td align="center"> 475
</td>
<td align="center"> 2000
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Riki" title="Riki"><img alt="Riki.png" src="/images/thumb/3/39/Riki.png/100px-Riki.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Riki" title="Riki">Riki</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2
</td>
<td align="center"> 34
</td>
<td align="center"> 2.9
</td>
<td align="center"> 14
</td>
<td align="center"> 1.3
</td>
<td align="center"> 300
</td>
<td align="center"> 5.76
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 52
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Rubick" title="Rubick"><img alt="Rubick.png" src="/images/thumb/3/37/Rubick.png/100px-Rubick.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Rubick" title="Rubick">Rubick</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.5
</td>
<td align="center"> 14
</td>
<td align="center"> 1.6
</td>
<td align="center"> 27
</td>
<td align="center"> 2.4
</td>
<td align="center"> 290
</td>
<td align="center"> 0.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 54
</td>
<td align="center"> 600
</td>
<td align="center"> 1125
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.1
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Sand_King" title="Sand King"><img alt="Sand King.png" src="/images/thumb/2/2c/Sand_King.png/100px-Sand_King.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Sand_King" title="Sand King">Sand King</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 2.6
</td>
<td align="center"> 19
</td>
<td align="center"> 2.1
</td>
<td align="center"> 16
</td>
<td align="center"> 1.8
</td>
<td align="center"> 300
</td>
<td align="center"> 2.66
</td>
<td align="center"> 1.7
</td>
<td align="center"> 43
</td>
<td align="center"> 59
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.53
</td>
<td align="center"> 0
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Shadow_Demon" title="Shadow Demon"><img alt="Shadow Demon.png" src="/images/thumb/9/9d/Shadow_Demon.png/100px-Shadow_Demon.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Shadow_Demon" title="Shadow Demon">Shadow Demon</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.9
</td>
<td align="center"> 18
</td>
<td align="center"> 2.2
</td>
<td align="center"> 26
</td>
<td align="center"> 2.7
</td>
<td align="center"> 295
</td>
<td align="center"> 2.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 53
</td>
<td align="center"> 57
</td>
<td align="center"> 500
</td>
<td align="center"> 900
</td>
<td align="center"> 0.36
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Shadow_Fiend" title="Shadow Fiend"><img alt="Shadow Fiend.png" src="/images/thumb/7/71/Shadow_Fiend.png/100px-Shadow_Fiend.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Shadow_Fiend" title="Shadow Fiend">Shadow Fiend</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 2
</td>
<td align="center"> 20
</td>
<td align="center"> 2.9
</td>
<td align="center"> 18
</td>
<td align="center"> 2
</td>
<td align="center"> 305
</td>
<td align="center"> 1.8
</td>
<td align="center"> 1.7
</td>
<td align="center"> 35
</td>
<td align="center"> 41
</td>
<td align="center"> 500
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.67
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Shadow_Shaman" title="Shadow Shaman"><img alt="Shadow Shaman.png" src="/images/thumb/1/11/Shadow_Shaman.png/100px-Shadow_Shaman.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Shadow_Shaman" title="Shadow Shaman">Shadow Shaman</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.6
</td>
<td align="center"> 16
</td>
<td align="center"> 1.6
</td>
<td align="center"> 21
</td>
<td align="center"> 3
</td>
<td align="center"> 285
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 47
</td>
<td align="center"> 54
</td>
<td align="center"> 500
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Silencer" title="Silencer"><img alt="Silencer.png" src="/images/thumb/4/43/Silencer.png/100px-Silencer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Silencer" title="Silencer">Silencer</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2.2
</td>
<td align="center"> 16
</td>
<td align="center"> 2.1
</td>
<td align="center"> 27
</td>
<td align="center"> 2.5
</td>
<td align="center"> 300
</td>
<td align="center"> 1.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 43
</td>
<td align="center"> 57
</td>
<td align="center"> 600
</td>
<td align="center"> 1000
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Skeleton_King" title="Skeleton King"><img alt="Skeleton King.png" src="/images/thumb/f/fc/Skeleton_King.png/100px-Skeleton_King.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Skeleton_King" title="Skeleton King">Skeleton King</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.9
</td>
<td align="center"> 18
</td>
<td align="center"> 1.7
</td>
<td align="center"> 13
</td>
<td align="center"> 1.6
</td>
<td align="center"> 300
</td>
<td align="center"> 3.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 54
</td>
<td align="center"> 56
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.56
</td>
<td align="center"> 0.35
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Slardar" title="Slardar"><img alt="Slardar.png" src="/images/thumb/7/7b/Slardar.png/100px-Slardar.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Slardar" title="Slardar">Slardar</a>
</td>
<td align="center"> 21
</td>
<td align="center"> 2.8
</td>
<td align="center"> 17
</td>
<td align="center"> 2.4
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 300
</td>
<td align="center"> 5.38
</td>
<td align="center"> 1.7
</td>
<td align="center"> 51
</td>
<td align="center"> 59
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.36
</td>
<td align="center"> 0.35
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Slark" title="Slark"><img alt="Slark.png" src="/images/thumb/e/e2/Slark.png/100px-Slark.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Slark" title="Slark">Slark</a>
</td>
<td align="center"> 21
</td>
<td align="center"> 1.8
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 16
</td>
<td align="center"> 1.9
</td>
<td align="center"> 305
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 56
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.001
</td>
<td align="center"> 1800
</td>
<td align="center"> 1800
</td></tr>

<tr>
<td><a href="/wiki/Sniper" title="Sniper"><img alt="Sniper.png" src="/images/thumb/8/8f/Sniper.png/100px-Sniper.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Sniper" title="Sniper">Sniper</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.7
</td>
<td align="center"> 21
</td>
<td align="center"> 2.9
</td>
<td align="center"> 15
</td>
<td align="center"> 2.6
</td>
<td align="center"> 290
</td>
<td align="center"> 1.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 36
</td>
<td align="center"> 42
</td>
<td align="center"> 550
</td>
<td align="center"> 3000
</td>
<td align="center"> 0.17
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 1000
</td></tr>

<tr>
<td><a href="/wiki/Spectre" title="Spectre"><img alt="Spectre.png" src="/images/thumb/9/90/Spectre.png/100px-Spectre.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Spectre" title="Spectre">Spectre</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 2
</td>
<td align="center"> 23
</td>
<td align="center"> 2.2
</td>
<td align="center"> 16
</td>
<td align="center"> 1.9
</td>
<td align="center"> 295
</td>
<td align="center"> 3.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 50
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Spirit_Breaker" title="Spirit Breaker"><img alt="Spirit Breaker.png" src="/images/thumb/8/82/Spirit_Breaker.png/100px-Spirit_Breaker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Spirit_Breaker" title="Spirit Breaker">Spirit Breaker</a>
</td>
<td align="center"> 29
</td>
<td align="center"> 2.4
</td>
<td align="center"> 17
</td>
<td align="center"> 1.7
</td>
<td align="center"> 14
</td>
<td align="center"> 1.8
</td>
<td align="center"> 290
</td>
<td align="center"> 5.38
</td>
<td align="center"> 1.7
</td>
<td align="center"> 60
</td>
<td align="center"> 70
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.6
</td>
<td align="center"> 0.47
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Storm_Spirit" title="Storm Spirit"><img alt="Storm Spirit.png" src="/images/thumb/2/25/Storm_Spirit.png/100px-Storm_Spirit.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Storm_Spirit" title="Storm Spirit">Storm Spirit</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 1.5
</td>
<td align="center"> 22
</td>
<td align="center"> 1.8
</td>
<td align="center"> 23
</td>
<td align="center"> 2.6
</td>
<td align="center"> 295
</td>
<td align="center"> 5.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 55
</td>
<td align="center"> 480
</td>
<td align="center"> 1100
</td>
<td align="center"> 0.5
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Sven" title="Sven"><img alt="Sven.png" src="/images/thumb/d/dd/Sven.png/100px-Sven.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Sven" title="Sven">Sven</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2.7
</td>
<td align="center"> 21
</td>
<td align="center"> 2
</td>
<td align="center"> 14
</td>
<td align="center"> 1.3
</td>
<td align="center"> 295
</td>
<td align="center"> 1.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 54
</td>
<td align="center"> 56
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Templar_Assassin" title="Templar Assassin"><img alt="Templar Assassin.png" src="/images/thumb/2/27/Templar_Assassin.png/100px-Templar_Assassin.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Templar_Assassin" title="Templar Assassin">Templar Assassin</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 2.1
</td>
<td align="center"> 23
</td>
<td align="center"> 2.7
</td>
<td align="center"> 20
</td>
<td align="center"> 2
</td>
<td align="center"> 305
</td>
<td align="center"> 4.22
</td>
<td align="center"> 1.7
</td>
<td align="center"> 53
</td>
<td align="center"> 59
</td>
<td align="center"> 140
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Tidehunter" title="Tidehunter"><img alt="Tidehunter.png" src="/images/thumb/6/6c/Tidehunter.png/100px-Tidehunter.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Tidehunter" title="Tidehunter">Tidehunter</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 3
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 16
</td>
<td align="center"> 1.7
</td>
<td align="center"> 310
</td>
<td align="center"> 3.1
</td>
<td align="center"> 1.7
</td>
<td align="center"> 47
</td>
<td align="center"> 53
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.6
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Timbersaw" title="Timbersaw"><img alt="Timbersaw.png" src="/images/thumb/8/81/Timbersaw.png/100px-Timbersaw.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Timbersaw" title="Timbersaw">Timbersaw</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.1
</td>
<td align="center"> 21
</td>
<td align="center"> 1.8
</td>
<td align="center"> 16
</td>
<td align="center"> 1.3
</td>
<td align="center"> 290
</td>
<td align="center"> 0.24
</td>
<td align="center"> 1.7
</td>
<td align="center"> 48
</td>
<td align="center"> 52
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.36
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Tinker" title="Tinker"><img alt="Tinker.png" src="/images/thumb/e/ec/Tinker.png/100px-Tinker.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Tinker" title="Tinker">Tinker</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 2
</td>
<td align="center"> 13
</td>
<td align="center"> 1.2
</td>
<td align="center"> 27
</td>
<td align="center"> 2.2
</td>
<td align="center"> 305
</td>
<td align="center"> 3.82
</td>
<td align="center"> 1.7
</td>
<td align="center"> 49
</td>
<td align="center"> 55
</td>
<td align="center"> 550
</td>
<td align="center"> 900
</td>
<td align="center"> 0.35
</td>
<td align="center"> 0.53
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Tiny" title="Tiny"><img alt="Tiny.png" src="/images/thumb/7/75/Tiny.png/100px-Tiny.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Tiny" title="Tiny">Tiny</a>
</td>
<td align="center"> 24
</td>
<td align="center"> 3
</td>
<td align="center"> 9
</td>
<td align="center"> 0.9
</td>
<td align="center"> 14
</td>
<td align="center"> 1.6
</td>
<td align="center"> 285
</td>
<td align="center"> 0.26
</td>
<td align="center"> 1.7
</td>
<td align="center"> 61
</td>
<td align="center"> 67
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.49
</td>
<td align="center"> 0.001
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Treant_Protector" title="Treant Protector"><img alt="Treant Protector.png" src="/images/thumb/1/18/Treant_Protector.png/100px-Treant_Protector.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Treant_Protector" title="Treant Protector">Treant Protector</a>
</td>
<td align="center"> 25
</td>
<td align="center"> 3.3
</td>
<td align="center"> 15
</td>
<td align="center"> 2
</td>
<td align="center"> 17
</td>
<td align="center"> 1.8
</td>
<td align="center"> 300
</td>
<td align="center"> 1.1
</td>
<td align="center"> 1.9
</td>
<td align="center"> 81
</td>
<td align="center"> 89
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.6
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 1200
</td></tr>

<tr>
<td><a href="/wiki/Undying" title="Undying"><img alt="Undying.png" src="/images/thumb/0/0d/Undying.png/100px-Undying.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Undying" title="Undying">Undying</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.1
</td>
<td align="center"> 10
</td>
<td align="center"> 0.8
</td>
<td align="center"> 27
</td>
<td align="center"> 2
</td>
<td align="center"> 310
</td>
<td align="center"> 3.4
</td>
<td align="center"> 1.7
</td>
<td align="center"> 57
</td>
<td align="center"> 65
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.45
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Ursa" title="Ursa"><img alt="Ursa.png" src="/images/thumb/a/a6/Ursa.png/100px-Ursa.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Ursa" title="Ursa">Ursa</a>
</td>
<td align="center"> 23
</td>
<td align="center"> 2.9
</td>
<td align="center"> 18
</td>
<td align="center"> 2.1
</td>
<td align="center"> 16
</td>
<td align="center"> 1.5
</td>
<td align="center"> 310
</td>
<td align="center"> 5.52
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 49
</td>
<td align="center"> 128
</td>
<td align="center">
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Vengeful_Spirit" title="Vengeful Spirit"><img alt="Vengeful Spirit.png" src="/images/thumb/7/78/Vengeful_Spirit.png/100px-Vengeful_Spirit.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Vengeful_Spirit" title="Vengeful Spirit">Vengeful Spirit</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 2.3
</td>
<td align="center"> 27
</td>
<td align="center"> 2.8
</td>
<td align="center"> 15
</td>
<td align="center"> 1.75
</td>
<td align="center"> 295
</td>
<td align="center"> 3.78
</td>
<td align="center"> 1.7
</td>
<td align="center"> 39
</td>
<td align="center"> 53
</td>
<td align="center"> 400
</td>
<td align="center"> 1500
</td>
<td align="center"> 0.33
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Venomancer" title="Venomancer"><img alt="Venomancer.png" src="/images/thumb/f/f0/Venomancer.png/100px-Venomancer.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Venomancer" title="Venomancer">Venomancer</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 1.85
</td>
<td align="center"> 22
</td>
<td align="center"> 2.6
</td>
<td align="center"> 18
</td>
<td align="center"> 1.75
</td>
<td align="center"> 290
</td>
<td align="center"> 3.08
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 48
</td>
<td align="center"> 450
</td>
<td align="center"> 900
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Viper" title="Viper"><img alt="Viper.png" src="/images/thumb/9/99/Viper.png/100px-Viper.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Viper" title="Viper">Viper</a>
</td>
<td align="center"> 20
</td>
<td align="center"> 1.9
</td>
<td align="center"> 21
</td>
<td align="center"> 2.5
</td>
<td align="center"> 15
</td>
<td align="center"> 1.8
</td>
<td align="center"> 285
</td>
<td align="center"> 1.94
</td>
<td align="center"> 1.7
</td>
<td align="center"> 44
</td>
<td align="center"> 46
</td>
<td align="center"> 575
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.33
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Visage" title="Visage"><img alt="Visage.png" src="/images/thumb/c/c2/Visage.png/100px-Visage.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Visage" title="Visage">Visage</a>
</td>
<td align="center"> 22
</td>
<td align="center"> 2.4
</td>
<td align="center"> 11
</td>
<td align="center"> 1.3
</td>
<td align="center"> 24
</td>
<td align="center"> 2.5
</td>
<td align="center"> 295
</td>
<td align="center"> 0.54
</td>
<td align="center"> 1.7
</td>
<td align="center"> 45
</td>
<td align="center"> 55
</td>
<td align="center"> 600
</td>
<td align="center"> 900
</td>
<td align="center"> 0.46
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Warlock" title="Warlock"><img alt="Warlock.png" src="/images/thumb/5/51/Warlock.png/100px-Warlock.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Warlock" title="Warlock">Warlock</a>
</td>
<td align="center"> 18
</td>
<td align="center"> 2.5
</td>
<td align="center"> 10
</td>
<td align="center"> 1
</td>
<td align="center"> 24
</td>
<td align="center"> 2.7
</td>
<td align="center"> 295
</td>
<td align="center"> 2.4
</td>
<td align="center"> 1.7
</td>
<td align="center"> 46
</td>
<td align="center"> 56
</td>
<td align="center"> 600
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.3
</td>
<td align="center"> 0.5
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Weaver" title="Weaver"><img alt="Weaver.png" src="/images/thumb/c/c3/Weaver.png/100px-Weaver.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Weaver" title="Weaver">Weaver</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 1.5
</td>
<td align="center"> 14
</td>
<td align="center"> 2.5
</td>
<td align="center"> 15
</td>
<td align="center"> 1.8
</td>
<td align="center"> 290
</td>
<td align="center"> 0.96
</td>
<td align="center"> 1.7
</td>
<td align="center"> 50
</td>
<td align="center"> 60
</td>
<td align="center"> 425
</td>
<td align="center"> 900
</td>
<td align="center"> 0.64
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Windrunner" title="Windrunner"><img alt="Windrunner.png" src="/images/thumb/e/e2/Windrunner.png/100px-Windrunner.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Windrunner" title="Windrunner">Windrunner</a>
</td>
<td align="center"> 15
</td>
<td align="center"> 2.5
</td>
<td align="center"> 17
</td>
<td align="center"> 1.4
</td>
<td align="center"> 22
</td>
<td align="center"> 2.6
</td>
<td align="center"> 295
</td>
<td align="center"> 1.38
</td>
<td align="center"> 1.5
</td>
<td align="center"> 44
</td>
<td align="center"> 56
</td>
<td align="center"> 600
</td>
<td align="center"> 1250
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.3
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Wisp" title="Wisp"><img alt="Wisp.png" src="/images/thumb/e/e7/Wisp.png/100px-Wisp.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Wisp" title="Wisp">Wisp</a>
</td>
<td align="center"> 17
</td>
<td align="center"> 1.9
</td>
<td align="center"> 14
</td>
<td align="center"> 1.6
</td>
<td align="center"> 23
</td>
<td align="center"> 1.7
</td>
<td align="center"> 295
</td>
<td align="center"> -0.04
</td>
<td align="center"> 1.7
</td>
<td align="center"> 43
</td>
<td align="center"> 52
</td>
<td align="center"> 575
</td>
<td align="center"> 1600
</td>
<td align="center"> 0.15
</td>
<td align="center"> 0.001
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Witch_Doctor" title="Witch Doctor"><img alt="Witch Doctor.png" src="/images/thumb/a/ac/Witch_Doctor.png/100px-Witch_Doctor.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Witch_Doctor" title="Witch Doctor">Witch Doctor</a>
</td>
<td align="center"> 16
</td>
<td align="center"> 1.8
</td>
<td align="center"> 13
</td>
<td align="center"> 1.4
</td>
<td align="center"> 24
</td>
<td align="center"> 2.9
</td>
<td align="center"> 305
</td>
<td align="center"> 0.82
</td>
<td align="center"> 1.7
</td>
<td align="center"> 51
</td>
<td align="center"> 61
</td>
<td align="center"> 600
</td>
<td align="center"> 1200
</td>
<td align="center"> 0.4
</td>
<td align="center"> 0.35
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>

<tr>
<td><a href="/wiki/Zeus" title="Zeus"><img alt="Zeus.png" src="/images/thumb/3/3c/Zeus.png/100px-Zeus.png" width="100" height="56" /></a>
</td>
<td align="center" style="font-weight:bold;"> <a href="/wiki/Zeus" title="Zeus">Zeus</a>
</td>
<td align="center"> 19
</td>
<td align="center"> 2.3
</td>
<td align="center"> 11
</td>
<td align="center"> 1.2
</td>
<td align="center"> 20
</td>
<td align="center"> 2.7
</td>
<td align="center"> 295
</td>
<td align="center"> 1.54
</td>
<td align="center"> 1.7
</td>
<td align="center"> 41
</td>
<td align="center"> 49
</td>
<td align="center"> 350
</td>
<td align="center"> 1100
</td>
<td align="center"> 0.633
</td>
<td align="center"> 0.4
</td>
<td align="center"> 1800
</td>
<td align="center"> 800
</td></tr>
</table>
<table class="navbox" cellspacing="0" style=";"><tr><td style="padding:2px;"><table cellspacing="0" class="nowraplinks hlist collapsible autocollapse" style="width:100%;background:transparent;color:inherit;;"><tr><th style=";" colspan="2" class="navbox-title"><span style="float:left;width:6em;text-align:left;"><div class="noprint plainlinks navbar" style="background:none; padding:0; font-weight:normal;;;background:none transparent;border:none;font-size:100%;; font-size:xx-small;"><a rel="nofollow" class="external text" href="http://www.dota2wiki.com/wiki/Template:MechanicsNav"><span title="View this template" style=";;background:none transparent;border:none;font-size:100%;">v</span></a>&#160;<span style="font-size:80%;">•</span>&#160;<a rel="nofollow" class="external text" href="http://www.dota2wiki.com/wiki/Template_talk:MechanicsNav"><span title="Discuss this template" style=";;background:none transparent;border:none;font-size:100%;">d</span></a>&#160;<span style="font-size:80%;">•</span>&#160;<a rel="nofollow" class="external text" href="http://www.dota2wiki.com/index.php?title=Template:MechanicsNav&amp;action=edit"><span title="Edit this template" style=";;background:none transparent;border:none;font-size:100%;;">e</span></a></div></span><span class="" style="font-size:110%;">
<a href="/wiki/Mechanics" title="Mechanics">Mechanics</a></span></th></tr><tr style="height:2px;"><td></td></tr><tr><td class="navbox-group" style=";;"><i>Hero</i></td><td style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px;;;" class="navbox-list navbox-odd"><div style="padding:0em 0.25em">
<ul><li> <a href="/wiki/Abilities" title="Abilities">Abilities</a>
</li><li> <a href="/wiki/Armor" title="Armor">Armor</a>
</li><li> <a href="/wiki/Attributes" title="Attributes">Attributes</a> (<a href="/wiki/Strength" title="Strength">Strength</a>/<a href="/wiki/Agility" title="Agility">Agility</a>/<a href="/wiki/Intelligence" title="Intelligence">Intelligence</a>)
</li><li> <a href="/wiki/Channeling" title="Channeling">Channeling</a>
</li><li> <a href="/wiki/Damage_Block" title="Damage Block">Damage Block</a>
</li><li> <a href="/wiki/Evasion" title="Evasion">Evasion</a>
</li><li> <a href="/wiki/Experience" title="Experience">Experience</a>
</li><li> <a href="/wiki/Health" title="Health">Health</a>
</li><li> <a href="/wiki/Illusions" title="Illusions">Illusions</a>
</li><li> <a href="/wiki/Invisibility" title="Invisibility">Invisibility</a>
</li><li> <a href="/wiki/Magic_immunity" title="Magic immunity">Magic immunity</a>
</li><li> <a href="/wiki/Magic_resistance" title="Magic resistance">Magic resistance</a>
</li><li> <a href="/wiki/Mana" title="Mana">Mana</a>
</li><li> <a href="/wiki/Movement_speed" title="Movement speed">Movement speed</a>
</li><li> <a href="/wiki/Teleport" title="Teleport">Teleport</a></div></td></tr><tr style="height:2px"><td></td></tr><tr><td class="navbox-group" style=";;"><i>Attack</i></td><td style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px;;;" class="navbox-list navbox-even"><div style="padding:0em 0.25em">
</li><li> <a href="/wiki/Attack_range" title="Attack range">Attack range</a>
</li><li> <a href="/wiki/Attack_speed" title="Attack speed">Attack speed</a>
</li><li> <a href="/wiki/Bash" title="Bash">Bash</a>
</li><li> <a href="/wiki/Cleave" title="Cleave">Cleave</a>
</li><li> <a href="/wiki/Critical_strike" title="Critical strike">Critical strike</a>
</li><li> <a href="/wiki/Damage_types" title="Damage types">Damage types</a>
</li><li> <a href="/wiki/Lifesteal" title="Lifesteal">Lifesteal</a>
</li><li> <a href="/wiki/Unique_Attack_Modifier" title="Unique Attack Modifier">Unique Attack Modifiers</a></div></td></tr><tr style="height:2px"><td></td></tr><tr><td class="navbox-group" style=";;"><i>Disables and status effects</i></td><td style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px;;;" class="navbox-list navbox-odd"><div style="padding:0em 0.25em">
</li><li> <a href="/wiki/Blind" title="Blind">Blind</a>
</li><li> <a href="/wiki/Cyclone" title="Cyclone">Cyclone</a>
</li><li> <a href="/wiki/Disable" title="Disable">Disable</a>
</li><li> <a href="/wiki/Disarm" title="Disarm">Disarm</a>
</li><li> <a href="/wiki/Entangle" title="Entangle">Entangle</a>
</li><li> <a href="/wiki/Ethereal" title="Ethereal">Ethereal</a>
</li><li> <a href="/wiki/Hex" title="Hex">Hex</a>
</li><li> <a href="/wiki/Pause" title="Pause">Pause</a>
</li><li> <a href="/wiki/Purge" title="Purge">Purge</a>
</li><li> <a href="/wiki/Silence" title="Silence">Silence</a>
</li><li> <a href="/wiki/Sleep" title="Sleep">Sleep</a>
</li><li> <a href="/wiki/Slow" title="Slow">Slow</a>
</li><li> <a href="/wiki/Stun" title="Stun">Stun</a>
</li><li> <a href="/wiki/Trap" title="Trap">Trap</a></div></td></tr><tr style="height:2px"><td></td></tr><tr><td class="navbox-group" style=";;"><i>World</i></td><td style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px;;;" class="navbox-list navbox-even"><div style="padding:0em 0.25em">
</li><li> <a href="/wiki/Buildings" title="Buildings">Buildings</a>
</li><li> <a href="/wiki/Gold" title="Gold">Gold</a>
</li><li> <a href="/wiki/Item_passive_stacking" title="Item passive stacking">Item passive stacking</a>
</li><li> <a href="/wiki/Item_sharing" title="Item sharing">Item sharing</a>
</li><li> <a href="/wiki/Pseudo-random_distribution" title="Pseudo-random distribution">Pseudo-random distribution</a>
</li><li> <a href="/wiki/Vision" title="Vision">Vision</a></div></td></tr><tr style="height:2px"><td></td></tr><tr><td class="navbox-group" style=";;"><i>Gameplay</i></td><td style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px;;;" class="navbox-list navbox-odd"><div style="padding:0em 0.25em">
</li><li> <a href="/wiki/Creep_control_techniques" title="Creep control techniques">Creep control techniques</a>
</li><li> <a href="/wiki/Ganking" title="Ganking">Ganking</a>
</li><li> <a href="/wiki/Harassment" title="Harassment">Harassment</a>
</li><li> <a href="/wiki/Jungling" title="Jungling">Jungling</a>
</li><li> <a href="/wiki/Lane" title="Lane">Lane</a>
</li><li> <a href="/wiki/Minimap" title="Minimap">Minimap</a>
</li><li> <a href="/wiki/Pushing" title="Pushing">Pushing</a>
</li><li> <a href="/wiki/Role" title="Role">Roles</a></div></td></tr></table></td></tr></table>
</li></ul>
<p><br />
</p>
<!-- 
NewPP limit report
Preprocessor node count: 19926/1000000
Post-expand include size: 132780/2097152 bytes
Template argument size: 15915/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key dota2wiki-dotawiki_:pcache:idhash:27839-0!*!0!*!*!2!* and timestamp 20121223125604 -->
</div>				<!-- /bodycontent -->
								<!-- printfooter -->
				<div class="printfooter">
				Retrieved from "<a href="http://www.dota2wiki.com/index.php?title=Table_of_Hero_attributes&amp;oldid=149867">http://www.dota2wiki.com/index.php?title=Table_of_Hero_attributes&amp;oldid=149867</a>"				</div>
				<!-- /printfooter -->
												<!-- catlinks -->
				<div id='catlinks' class='catlinks catlinks-allhidden'></div>				<!-- /catlinks -->
												<div class="visualClear"></div>
				<!-- debughtml -->
								<!-- /debughtml -->

                <div style="text-align: center; padding: 5px; width: 1200px; margin: 0 auto;" class="btflb">
                    <!-- Begin Advertising // Tag for network 5259: Curse.com // Website: dota2wiki // Page: Default // Placement: Dota2wiki_Default_Below_728x90 (2226916) // created at: Nov 3, 2011 2:31:01 PM -->
                    <script language="javascript">
                        <!--
                        if (window.adgroupid == undefined) {
                            window.adgroupid = Math.round(Math.random() * 1000);
                        }
                        document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtechus.com/addyn/3.0/5259.1/2226916/0/225/ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
                        //-->
                    </script><noscript><a href="http://adserver.adtechus.com/adlink/3.0/5259.1/2226916/0/225/ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtechus.com/adserv/3.0/5259.1/2226916/0/225/ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
                    <!-- End Advertising -->
                </div>

			</div>
			<!-- /bodyContent -->
		</div>
		<!-- /content -->
		<!-- header -->
		<div id="mw-head" class="noprint">
			
<!-- 0 -->
<div id="p-personal" class="">
	<h5>Personal tools</h5>
	<ul>
		<li id="pt-login"><a href="/index.php?title=Special:UserLogin&amp;returnto=Table+of+Hero+attributes" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in / create account</a></li>
	</ul>
</div>

<!-- /0 -->
			<div id="left-navigation">
				
<!-- 0 -->
<div id="p-namespaces" class="vectorTabs">
	<h5>Namespaces</h5>
	<ul>
					<li  id="ca-nstab-main" class="selected"><span><a href="/wiki/Table_of_Hero_attributes"  title="View the content page [c]" accesskey="c">Page</a></span></li>
					<li  id="ca-talk"><span><a href="/wiki/Talk:Table_of_Hero_attributes"  title="Discussion about the content page [t]" accesskey="t">Discussion</a></span></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-variants" class="vectorMenu emptyPortlet">
		<h5><span>Variants</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->
			</div>
			<div id="right-navigation">
				
<!-- 0 -->
<div id="p-views" class="vectorTabs">
	<h5>Views</h5>
	<ul>
					<li id="ca-view" class="selected"><span><a href="/wiki/Table_of_Hero_attributes" >Read</a></span></li>
					<li id="ca-edit"><span><a href="/index.php?title=Table_of_Hero_attributes&amp;action=edit"  title="You can edit this page. Please use the preview button before saving [e]" accesskey="e">Edit</a></span></li>
					<li id="ca-history" class="collapsible"><span><a href="/index.php?title=Table_of_Hero_attributes&amp;action=history"  title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>
			</ul>
</div>

<!-- /0 -->

<!-- 1 -->
<div id="p-cactions" class="vectorMenu emptyPortlet">
	<h5><span>Actions</span><a href="#"></a></h5>
	<div class="menu">
		<ul>
					</ul>
	</div>
</div>

<!-- /1 -->

<!-- 2 -->
<div id="p-search">
	<h5><label for="searchInput">Search</label></h5>
	<form action="/index.php" id="searchform">
		<input type='hidden' name="title" value="Special:Search"/>
				<input type="search" name="search" title="Search Dota 2 Wiki [f]" accesskey="f" id="searchInput" />		<input type="submit" name="go" value="Go" title="Go to a page with this exact name if exists" id="searchGoButton" class="searchButton" />		<input type="submit" name="fulltext" value="Search" title="Search the pages for this text" id="mw-searchButton" class="searchButton" />			</form>
</div>

<!-- /2 -->
			</div>
		</div>
		<!-- /header -->
		<!-- panel -->
			<div id="mw-panel" class="noprint">
				<!-- logo -->
					<div id="p-logo"><a style="background-image: url(http://www.dota2wiki.com/images/dota2wikilogo.png);" href="/wiki/Dota_2_Wiki"  title="Visit the main page"></a></div>
				<!-- /logo -->
				
<!-- navigation -->
<div class="portal" id='p-navigation'>
	<h5>Navigation</h5>
	<div class="body">
		<ul>
			<li id="n-mainpage-description"><a href="/wiki/Dota_2_Wiki" title="Visit the main page [z]" accesskey="z">Main page</a></li>
			<li id="n-Heroes"><a href="/wiki/Heroes">Heroes</a></li>
			<li id="n-Items"><a href="/wiki/Items">Items</a></li>
			<li id="n-Store"><a href="/wiki/Dota_2_Store">Store</a></li>
		</ul>
	</div>
</div>

<!-- /navigation -->

<!-- Competitive Scene -->
<div class="portal" id='p-Competitive_Scene'>
	<h5>Competitive Scene</h5>
	<div class="body">
		<ul>
			<li id="n-Players"><a href="/wiki/Players">Players</a></li>
			<li id="n-Teams"><a href="/wiki/Teams">Teams</a></li>
			<li id="n-Tournaments"><a href="/wiki/Tournaments">Tournaments</a></li>
		</ul>
	</div>
</div>

<!-- /Competitive Scene -->

<!-- Wiki -->
<div class="portal" id='p-Wiki'>
	<h5>Wiki</h5>
	<div class="body">
		<ul>
			<li id="n-Discussion"><a href="/wiki/Dota_2_Wiki:Discussion">Discussion</a></li>
			<li id="n-Translate"><a href="/wiki/Help:Language_translation">Translate</a></li>
			<li id="n-IRC-channel"><a href="/wiki/Dota_2_Wiki:IRC">IRC channel</a></li>
			<li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li>
			<li id="n-help"><a href="/wiki/Help:Contents" title="The place to find out">Help</a></li>
		</ul>
	</div>
</div>

<!-- /Wiki -->

<!-- SEARCH -->

<!-- /SEARCH -->

<!-- TOOLBOX -->
<div class="portal" id='p-tb'>
	<h5>Toolbox</h5>
	<div class="body">
		<ul>
			<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Table_of_Hero_attributes" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li>
			<li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Table_of_Hero_attributes" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li>
			<li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li>
			<li><a href="/index.php?title=Table_of_Hero_attributes&amp;printable=yes" rel="alternate">Printable version</a></li>
			<li id="t-permalink"><a href="/index.php?title=Table_of_Hero_attributes&amp;oldid=149867" title="Permanent link to this revision of the page">Permanent link</a></li>
<li id="t-smwbrowselink"><a href="/wiki/Special:Browse/Table_of_Hero_attributes" title="Special:Browse/Table of Hero attributes">Browse properties</a></li>		</ul>
	</div>
</div>

<!-- /TOOLBOX -->

<!-- Languages -->
<div class="portal" id='p-Languages'>
	<h5>Languages</h5>
	<div class="body">
		<ul>
			<li id="n-English"><a href="/wiki/Table_of_Hero_attributes">English</a></li>
			<li id="n-.D0.A0.D1.83.D1.81.D1.81.D0.BA.D0.B8.D0.B9"><a href="/wiki/Table_of_Hero_attributes/ru">Русский</a></li>
		</ul>
	</div>
</div>

<!-- /Languages -->

<!-- Dota 2 -->
<div class="portal" id='p-Dota_2'>
	<h5>Dota 2</h5>
	<div class="body">
		<ul>
			<li id="n-Dota-2-Hub"><a href="http://steamcommunity.com/app/570" rel="nofollow">Dota 2 Hub</a></li>
			<li id="n-Blog"><a href="http://blog.dota2.com" rel="nofollow">Blog</a></li>
			<li id="n-Dota-2-Store"><a href="http://www.dota2.com/store/" rel="nofollow">Dota 2 Store</a></li>
			<li id="n-PlayDota"><a href="http://www.playdota.com/" rel="nofollow">PlayDota</a></li>
			<li id="n-Forums"><a href="http://www.playdota.com/forums/" rel="nofollow">Forums</a></li>
			<li id="n-Facebook"><a href="http://www.facebook.com/pages/Dota-2/106876872711112" rel="nofollow">Facebook</a></li>
			<li id="n-Twitter"><a href="http://twitter.com/#!/dota2" rel="nofollow">Twitter</a></li>
		</ul>
	</div>
</div>

<!-- /Dota 2 -->

<!-- Communities -->
<div class="portal" id='p-Communities'>
	<h5>Communities</h5>
	<div class="body">
		<ul>
			<li id="n-GosuGamers"><a href="http://www.gosugamers.net/dota2" rel="nofollow">GosuGamers</a></li>
			<li id="n-joinDOTA"><a href="http://www.joindota.com" rel="nofollow">joinDOTA</a></li>
			<li id="n-Reddit"><a href="http://reddit.com/r/dota2" rel="nofollow">Reddit</a></li>
			<li id="n-Team-Liquid"><a href="http://www.teamliquid.net/dota2/" rel="nofollow">Team Liquid</a></li>
		</ul>
	</div>
</div>

<!-- /Communities -->

<!-- LANGUAGES -->

<!-- /LANGUAGES -->
			</div>
		<!-- /panel -->
		<!-- sidepanel -->
		            <div id="curse-panel">
                <!-- Recent Articles block -->
                <div class="infobox">
                    <div class="block">
                        <h2 class='block_header'>Recent Community Articles</h2>
                        <div id="mcfrss"></div>
                    </div>
                </div>
                <!-- End Recent Articles block -->
                <!-- 300x250 Ad block -->
                <div class="infobox atfmrec">	
					<!--Standard Javascript Tag (GroupID) // Tag for network 5259: Curse.com // Website: Dota2wiki // Page: Default // Placement: Dota2wiki_Default_Above_300x250 (2226918) // created at: Sep 19, 2012 12:52:34 PM-->
					<script language="javascript">
					<!--
					if (window.adgroupid == undefined) {
						window.adgroupid = Math.round(Math.random() * 1000);
					}
					document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtechus.com/addyn/3.0/5259.1/2226918/0/170/ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
					//-->
					</script><noscript><a href="http://adserver.adtechus.com/adlink/3.0/5259.1/2226918/0/170/ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtechus.com/adserv/3.0/5259.1/2226918/0/170/ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="300" height="250"></a></noscript>
					<!-- End of JavaScript Tag -->
				</div>
                <!-- End 400x250 Ad block -->
                <!-- Twitter block -->
                <div class="infobox">
                    <div class="block">
                        <h2 class='block_header'><a href="http://twitter.com/#!/DOTA2" title="DOTA2's Twitter" class="goto" target="_blank">Dota2 Tweets</a></h2>
                        <ul id="twitter_posts">Getting your tweets...</ul>

                    </div>
                </div>
                <!-- End Twitter block -->
            </div>
            </div>
                	<!-- /sidepanel -->
		<!-- footer -->
		<div id="footer">
							<ul id="footer-info">
											<li id="footer-info-lastmod"> This page was last modified on 9 September 2012, at 16:13.</li>
											<li id="footer-info-copyright">Content is available under <a href="/wiki/Dota_2_Wiki" title="Dota 2 Wiki">CC BY-NC-SA 3.0</a>.</li>
									</ul>
							<ul id="footer-places">
											<li id="footer-places-privacy"><a href="/wiki/Dota_2_Wiki:Privacy_policy" title="Dota 2 Wiki:Privacy policy">Privacy policy</a></li>
											<li id="footer-places-about"><a href="/wiki/Dota_2_Wiki:About" title="Dota 2 Wiki:About">About Dota 2 Wiki</a></li>
											<li id="footer-places-disclaimer"><a href="/wiki/Dota_2_Wiki:General_disclaimer" title="Dota 2 Wiki:General disclaimer">Disclaimers</a></li>
									</ul>
										<ul id="footer-icons" class="noprint">
					<li id="footer-copyrightico">
						<a href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" alt="CC BY-NC-SA 3.0" width="88" height="31" /></a>
					</li>
					<li id="footer-poweredbyico">
						<a href="http://www.mediawiki.org/"><img src="/skins/common/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" width="88" height="31" /></a>
						<a href="http://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki"><img src="/extensions/SemanticMediaWiki/skins/images/smw_button.png" alt="Powered by Semantic MediaWiki" width="88" height="31" /></a>
					</li>
				</ul>
						<div style="clear:both"></div>
		</div>
		<!-- /footer -->
		<!-- fixalpha -->
		<script type="text/javascript"> if ( window.isMSIE55 ) fixalpha(); </script>
		<!-- /fixalpha -->
		<script src="/load.php?debug=false&amp;lang=en&amp;modules=skins.vector&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
	mw.loader.load(["mediawiki.user", "mediawiki.util", "mediawiki.page.ready", "mediawiki.legacy.wikibits", "mediawiki.legacy.ajax", "mediawiki.legacy.mwsuggest"]);
}
</script>
<script src="/skins/common/jquery.min.js?303"></script>
<script src="/skins/common/jquery.twitter.js?303"></script>
<script>/*<![CDATA[*/
jQuery(function(){
                           jQuery.jTwitter('DOTA2', 6, function(data){
                               var posts = jQuery('#twitter_posts');
                               posts.empty();
                               jQuery.each(data, function(i, post) {
                                   posts.append('<li class=\'post\'>' + post.text + '</li>');
                               });
                           });
                       });
/*]]>*/</script>
<script src="/skins/common/jquery.zrssfeed.min.js?303"></script>
<script>
 jQuery(document).ready(function () {
                                    jQuery('#mcfrss').rssfeed('http://blog.dota2.com/rss', {
                                        limit: 5,
                                        header:false,
                                        content: false,
                                        snippet: false
                                    });
                                });
</script>
<script src="/load.php?debug=false&amp;lang=en&amp;modules=site&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
	mw.user.options.set({"ccmeonemails":0,"cols":80,"date":"default","diffonly":0,"disablemail":0,"disablesuggest":0,"editfont":"default","editondblclick":0,"editsection":1,"editsectiononrightclick":0,"enotifminoredits":0,"enotifrevealaddr":0,"enotifusertalkpages":1,"enotifwatchlistpages":0,"extendwatchlist":0,"externaldiff":0,"externaleditor":0,"fancysig":0,"forceeditsummary":0,"gender":"unknown","hideminor":0,"hidepatrolled":0,"highlightbroken":1,"imagesize":2,"justify":0,"math":1,"minordefault":0,"newpageshidepatrolled":0,"nocache":0,"noconvertlink":0,"norollbackdiff":0,"numberheadings":0,"previewonfirst":0,"previewontop":1,"quickbar":5,"rcdays":7,"rclimit":50,"rememberpassword":0,"rows":25,"searchlimit":20,"showhiddencats":0,"showjumplinks":1,"shownumberswatching":1,"showtoc":1,"showtoolbar":1,"skin":"vector","stubthreshold":0,"thumbsize":2,"underline":2,"uselivepreview":0,"usenewrc":0,"watchcreations":0,"watchdefault":0,"watchdeletion":0,"watchlistdays":3,"watchlisthideanons":0,
	"watchlisthidebots":0,"watchlisthideliu":0,"watchlisthideminor":0,"watchlisthideown":0,"watchlisthidepatrolled":0,"watchmoves":0,"wllimit":250,"usebetatoolbar":1,"usebetatoolbar-cgd":1,"variant":"en","language":"en","searchNs0":true,"searchNs1":false,"searchNs2":false,"searchNs3":false,"searchNs4":false,"searchNs5":false,"searchNs6":false,"searchNs7":false,"searchNs8":false,"searchNs9":false,"searchNs10":false,"searchNs11":false,"searchNs12":false,"searchNs13":false,"searchNs14":false,"searchNs15":false,"searchNs102":false,"searchNs103":false,"searchNs108":false,"searchNs109":false,"searchNs500":false,"searchNs501":false});;mw.user.tokens.set({"editToken":"+\\","watchToken":false});;mw.loader.state({"user.options":"ready","user.tokens":"ready"});
	
	/* cache key: dota2wiki-dotawiki_:resourceloader:filter:minify-js:4:3537adfe0c3d3207b2c1d1b2c20fc0a2 */
}
</script>         <div id="ft">
                    <div class="site-navigation">
                        <ul class="navigation-horizontal">
                         <li>&copy; 2006-2012<a href="http://www.curse.com/content/AboutCurse.aspx"> Curse, Inc. </a></li><li>Dota 2 content and materials are trademarks and copyrights of Valve or its licensors. All rights reserved. 
            This site is a part of Curse, Inc. and is not affiliated with Valve.</li></ul></div>
                    <div class="network-navigation">
                        <ul class="curse">
                            <li class="header"><a href="http://www.curse.com/">Curse</a></li>
                                <li><a href="mailto:contact@curse.com">Contact</a>
                                <li><a href="http://www.curse.com/advertising/overview">Advertising</a></li>
                                <li><a href="http://www.curse.com/premium">Curse Premium</a></li>
                                <li><a href="http://www.curse.com/terms">Terms of Service</a></li>
                                <li><a href="http://www.curse.com/privacy">Privacy Policy</a></li>
                                <li><a href="http://www.curse.com/jobs">Careers</a></li>
                        </ul><ul class="core"><li class="header">Core</li><li><a href="http://www.curse.com/" target="_blank">Curse</a></li><li><a href="http://www.curseforge.com/" target="_blank">CurseForge</a></li><li><a href="http://dev.bukkit.org/" target="_blank">BukkitDev</a></li><li><a href="http://www.lolpro.com/" target="_blank">LoL Pro</a></li><li><a href="http://www.mmo-champion.com/" target="_blank">MMO-Champion</a></li><li><a href="http://www.sc2mapster.com/" target="_blank">SC2Mapster</a></li><li><a href="http://www.wowace.com/" target="_blank">WowAce</a></li><li><a href="http://www.wowstead.com/" target="_blank">WowStead</a></li></ul><ul class="database"><li class="header">Database</li><li><a href="http://www.aionarmory.com/" target="_blank">AionArmory</a></li><li><a href="http://db.darthhater.com/" target="_blank">DarthHaterDB</a></li><li><a href="http://www.gw2db.com/" target="_blank">Guild Wars 2 DB</a></li><li><a href="http://www.wowdb.com/" target="_blank">WOWDB</a></li><li><a href="http://www.zybez.net/" target="_blank">Zybez</a></li></ul><ul class="community double"><li class="header">Community</li><li><a href="http://www.aionsource.com/" target="_blank">AionSource</a></li><li><a href="http://www.arenajunkies.com/" target="_blank">Arena Junkies</a></li><li><a href="http://www.bladeandsouldojo.com/" target="_blank">Blade & Soul Dojo</a></li><li><a href="http://www.darthhater.com/" target="_blank">DarthHater</a></li><li><a href="http://www.diablofans.com/" target="_blank">DiabloFans</a></li><li><a href="http://www.enterbf3.com/" target="_blank">Enter BF3</a></li><li><a href="http://www.ffxivcore.com/" target="_blank">FFXIVCore</a></li><li><a href="http://www.fm-base.co.uk/forum/forum.php" target="_blank">FM Base</a></li><li><a href="http://www.fpsgeneral.com/" target="_blank">FPS General</a></li><li><a href="http://www.guildwars2guru.com/" target="_blank">Guild Wars 2 Guru</a></li><li><a href="http://www.guildwarsguru.com/" target="_blank">Guild Wars Guru</a></li><li><a href="http://www.minecraftforum.net/" target="_blank">Minecraft Forum</a></li><li><a href="http://www.reignofgaming.net/" target="_blank">Reign of Gaming</a></li><li><a href="http://www.scrollsfans.com/" target="_blank">Scrolls Fans</a></li><li><a href="http://www.terafans.com/" target="_blank">TERA Fans</a></li><li><a href="http://www.terrariaonline.com/" target="_blank">Terraria Online</a></li><li><a href="http://www.whalliance.com/" target="_blank">WH Alliance</a></li></ul><ul class="wiki double"><li class="header">Wiki</li><li><a href="http://www.the0x10cwiki.net/" target="_blank">0x10c Wiki</a></li><li><a href="http://www.archeagewiki.com/" target="_blank">ArcheAge Wiki</a></li><li><a href="http://www.bladeandsoulwiki.com/" target="_blank">Blade & Soul Wiki</a></li><li><a href="http://www.bl2wiki.com/" target="_blank">Borderlands 2 Wiki</a></li><li><a href="http://www.brickforcewiki.com/" target="_blank">Brick-Force Wiki</a></li><li><a href="http://www.cabalwiki.com/" target="_blank">Cabal Wiki</a></li><li><a href="http://www.castlestorywiki.com/" target="_blank">Castle Story Wiki</a></li><li><a href="http://www.cobaltwiki.com/" target="_blank">Cobalt Wiki</a></li><li><a href="http://www.cubewiki.net/" target="_blank">Cube World Wiki</a></li><li><a href="http://dayzwiki.com/" target="_blank">DayZ Wiki</a></li><li><a href="http://www.diablowiki.com/" target="_blank">Diablo Wiki</a></li><li><a href="http://www.dishonoredwiki.net/" target="_blank">Dishonored Wiki</a></li><li><a href="http://www.dota2wiki.com/" target="_blank">Dota 2 Wiki</a></li><li><a href="http://www.dragonnestwiki.com/" target="_blank">Dragon Nest Wiki</a></li><li><a href="http://www.theevonywiki.com/" target="_blank">Evony Wiki</a></li><li><a href="http://www.falloutwiki.com/" target="_blank">Fallout Wiki</a></li><li><a href="http://wiki.ffxivcore.com/" target="_blank">FFXIVCore Wiki</a></li><li><a href="http://www.gomewiki.com/" target="_blank">GoME Wiki</a></li><li><a href="http://www.guildwiki.org/" target="_blank">GuildWiki</a></li><li><a href="http://leaguepedia.com/" target="_blank">Leaguepedia</a></li><li><a href="http://www.minecraftwiki.net/" target="_blank">Minecraft Wiki</a></li><li><a href="http://www.ps2wiki.net/" target="_blank">PlanetSide 2 Wiki</a></li><li><a href="http://www.gwpvx.com/" target="_blank">PvXwiki</a></li><li><a href="http://www.theromwiki.com/" target="_blank">Runes of Magic Wiki</a></li><li><a href="http://www.scrollswiki.net/" target="_blank">Scrolls Wiki</a></li><li><a href="http://www.skyrimwiki.com/" target="_blank">Skyrim Wiki</a></li><li><a href="http://www.smitewiki.com/" target="_blank">Smite Wiki</a></li><li><a href="http://www.starboundwiki.com/" target="_blank">Starbound Wiki</a></li><li><a href="http://www.stowiki.org/" target="_blank">STO Wiki</a></li><li><a href="http://wiki.terafans.com/" target="_blank">TERA Fans Wiki</a></li><li><a href="http://www.telarapedia.com/" target="_blank">Telarapedia</a></li><li><a href="http://wiki.terrariaonline.com/" target="_blank">Terraria Wiki</a></li><li><a href="http://www.tesowiki.com/" target="_blank">TESO Wiki</a></li><li><a href="http://www.secretworldwiki.com/" target="_blank">TSW Wiki</a></li><li><a href="http://www.vindictuswiki.com/" target="_blank">Vindictus Wiki</a></li><li><a href="http://www.warzwiki.com/" target="_blank">The War Z Wiki</a></li><li><a href="http://wasteland.falloutwiki.com/" target="_blank">Wasteland 2 Wiki</a></li><li><a href="http://www.wikiswtor.com/" target="_blank">WikiSWTOR</a></li><li><a href="http://www.wowpedia.org/" target="_blank">Wowpedia</a></li><li><a href="http://www.xcomwiki.net/" target="_blank">XCOM Wiki</a></li></ul></div></div><!-- Begin Quantcast -->
<script type="text/javascript">
var _qevents = _qevents || [];
(function() {
   var elem = document.createElement('script');
   elem.src = (document.location.protocol == "https:" ? "https://secure" : "http://edge") + ".quantserve.com/quant.js";
   elem.async = true;
   elem.type = "text/javascript";
   var scpt = document.getElementsByTagName('script')[0];
   scpt.parentNode.insertBefore(elem, scpt);
})();
_qevents.push({qacct: "p-d2K9aGgyU-tIA"});
</script>
<noscript>
   <div style="display:none;"><img src="//pixel.quantserve.com/pixel/p-d2K9aGgyU-tIA.gif" border="0" height="1" width="1" alt="Quantcast" /></div>
</noscript>
<!-- End Quantcast -->

<!-- Begin comScore -->
<script>
var _comscore = _comscore || [];
_comscore.push({ c1: "2", c2: "6035118" });
(function() {
   var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
   s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
   el.parentNode.insertBefore(s, el);
})();
</script>
<noscript>
   <img src="http://b.scorecardresearch.com/p?c1=2&amp;c2=6035118&amp;cv=2.0&amp;cj=1" />
</noscript>
<!-- End comScore -->

<!-- Begin Nielsen -->
<script type="text/javascript">
(function () {
   var d = new Image(1, 1);
   d.onerror = d.onload = function () {
       d.onerror = d.onload = null;
   };
   d.src = ["//secure-us.imrworldwide.com/cgi-bin/m?ci=us-603339h&cg=0&cc=1&si=", escape(window.location.href), "&rp=", escape(document.referrer), "&ts=compact&rnd=", (new Date()).getTime()].join('');
})();
</script>
<noscript>
   <div><img src="//secure-us.imrworldwide.com/cgi-bin/m?ci=us-603339h&amp;cg=0&amp;cc=1&amp;ts=noscript" width="1" height="1" alt="" /></div>
</noscript>
<!-- End Nielsen --><!-- Served in 0.320 secs. -->
    <!-- Begin Google Analytics -->
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(
            ['_setAccount', 'UA-26524418-3'],
            ['_setDomainName', 'dota2wiki.com'],
            ['_addIgnoredRef', 'dota2wiki.com'],
            ['_trackPageview'],
            ['b._setAccount', 'UA-1045810-22'],
            ['b._setDomainName', 'dota2wiki.com'],
            ['b._addIgnoredRef', 'dota2wiki.com'],
            ['b._trackPageview']
        );
        (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
    <!-- End Google Analytics -->


	</body>
</html>

"""

pattern = r'<a href="/wiki/[\w\-]+" title="([\w \-]+)">\1</a>(.*?)</tr>'
regxp = re.compile(pattern, re.DOTALL)
conn = sqlite3.connect("./Dota2BBQ.db")
c = conn.cursor()
for hero in regxp.findall(data):
	hero_name = hero[0]
	c.execute('SELECT * FROM Heroes WHERE Name = ?', (hero_name, ))
	if c.fetchone():
		stats = re.findall(r'> ([\d.]+)\s<', hero[1])
		c.execute("UPDATE Heroes SET BasicStr = ?, BasicAgi = ?, BasicInt = ?, StrInc = ?, AgiInc = ?, IntInc = ?, Movement = ?, Armor = ?, MinDamage = ?, MaxDamage = ? WHERE Name = ?", (stats[0], stats[2], stats[4], stats[1], stats[3], stats[5], stats[6], stats[7], stats[9], stats[10], hero_name))
		conn.commit()
	
