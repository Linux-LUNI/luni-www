from django.http import HttpResponse


def Calendar(request):
	html = """<iframe src="https://www.google.com/calendar/embed?title=FLOSS_Events_In_Chicago&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=luni%40luni.org&amp;color=%23182C57&amp;src=hhlp4gcgvdmifq5lcbk7e27om4%40group.calendar.google.com&amp;color=%23125A12&amp;ctz=America%2FChicago" style=" border-width:0 " width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
	html = getHeader() + html + getSocialHTML()
	return HttpResponse(html)

def MailingLists(request):
	html = """
		For general info please mail to <a href="mailto:info@luni.org">info@luni.org</a>
		<p>
		We have two active <b>mailing lists</b>:
		
		<ul>
		<blockquote>
		<!-- Begin LUNI -->
		<table border=0 style="padding: 5px;" cellspacing=0>
		  <tr><td style="padding-left: 5px">
		  <b>Subscribe to <a href="https://groups.google.com/group/luni-chicago/">Linux Users of Northern Illinois</a></b>
		  </td></tr>
		  <form action="http://groups.google.com/group/luni-chicago/boxsubscribe">
		  <input type=hidden name="hl" value="en">
		  <tr><td style="padding-left: 5px;">
		  Email: <input type=text name=email>
		  <input type=submit name="sub" value="Subscribe">
		  </td></tr>
		</form>
		</table>
		
		<!-- End LUNI -->
		
		<!-- LUNI Announce -->
		<p>
		<table border=0 style=" padding: 5px;" cellspacing=0>
		  <tr><td style="padding-left: 5px">
		  <b>Subscribe to <a href="https://groups.google.com/group/luni-announce-chicago">Linux Users of Northern Illinois announce list</a></b>
		  </td></tr>
		  <form action="http://groups.google.com/group/luni-announce-chicago/boxsubscribe">
		  <input type=hidden name="hl" value="en">
		  <tr><td style="padding-left: 5px;">
		  Email: <input type=text name=email>
		  <input type=submit name="sub" value="Subscribe">
		  </td></tr>
		</form>
		</table>
		<!-- End LUNI Announce -->
		
		<li> <a href="http://www.facebook.com/pages/Linux-Users-of-Northern-Illinois/142456219162668"> Facebook Page </a> </li>
		<li> <a href="http://www.twitter.com/luni_announce"> Twitter Feed </a> rebroadcasts content of facebookpage.</li>
		<li> <a href="http://www.linkedin.com/groups?gid=160786&mostPopular=&trk=tyah"> LinkedIn Group </a></li>
		<li><a href="https://plus.google.com/b/117141677404718615863/"> Google Plus Page </a></li>
		<li> <a href="http://embed.mibbit.com/?server=irc.freenode.org&channel=%23luni&noServerNotices=true&noServerMotd=true">web-based chat client</a>
		
		</blockquote>
		</ul>

		<hr/>
		<h3> Old Archives</h3>
		<ul>
		<li> <a href="http://luni.org/pipermail/luni/"> Luni Archives</a> </li>
		<li> <a href="http://luni.org/pipermail/luni-anounce/"> Luni Announcements Archives</a> </li>
		</ul>

	"""

	html = getHeader() + html + getSocialHTML()
	return HttpResponse(html )

def Organizations(request):
	html = """
		<i>FLOSS groups</i>
		<ul>
		
		<li><a href="http://groups.google.com/group/chicagolinux-discuss"> Chicago Linux Users</a></li>
		<li><a href="http://linux.depaul.edu/"> Depaul Linux Community (Defunct?) </a></li>
		<li><a href="http://nwclug.harpercollege.edu/">NorthWest Chicagoland Linux User Group</a></li>
		<li> <a href="http://ufo.chicago.il.us/"> Users of Free Operating systems</a></li>
		<li><a href="http://wclug.org/">  Windy City Linux Users Group </a></li>
		</ul>
		
		
		<i>General Geek groups</i>
		<ul>
		<li><a href="http://twitter.com/#!/chicagonerds">Chicago Nerds Social</a></li>
		<li><a href="http://www.freegeekchicago.org/">Free Geek Chicago</a></li>
		</ul>
		
		
		
		<i>Maker Spaces/Hacking groups</i>
		<ul>
		<li><a href="http://www.chicago2600.net/"> Chicago 2600 Group </a></li>
		<li><a href="http://pumpingstationone.org/"> Pumping Station One (Hackerspace )</a></li>
		<li><i>Programming Languages:</i></li>
		<ul>
		<li><a href="http://www.cjug.org/">Chicago Java</a></li>
		<li><a href="http://chipy.org/">Chicago Python</a></li>
		<li><a href="http://www.chirb.org/">Chicago Ruby</a></li>
		</ul>
		</ul>
	      """

	html = getHeader() + html + getSocialHTML()
	return HttpResponse(html)

def getSocialHTML():
	html = """
		<hr/>
		<!-- Place this tag in the <head> of your document-->
		<link href="https://plus.google.com/117141677404718615863/" rel="publisher" />
		
		<!-- Place this tag where you want the badge to render-->
		<a href="https://plus.google.com/117141677404718615863/?prsrc=3" style="text-decoration: none;"><img src="https://ssl.gstatic.com/images/icons/gplus-32.png" width="32" height="32" style="border: 0;"/></a>
		"""
	return html

def getHeader():
	html = """
		<h1> Linux Users of Northern Illinois (Chicago)  </h1><br/>
		<a href="/calendar/">Calendar</a> | <a href="/mailing/"> MailingList </a> | <a href="/orgs/"> Organizations </a>   
		<br/><hr>
		"""
	return html
