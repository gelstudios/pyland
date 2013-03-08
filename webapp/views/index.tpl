<title>tinybbs</title>
<div class=topbar>
<h1>tinybbs messages</h1>
</div>

%for msg in messages:
	<div class=message>
	<b>Poster:</b> {{msg.get('account','Anon')}}
	<br>
	<b>status:</b> {{msg.get('status','new')}}
	<br>
	<b>message:</b> {{msg.get('msg', '...')}}
	<br>
	</div>
	<br>
%end

<br>
<form action="/postmsg" method="get"> <!--# method="post"-->
	Account: <input type="text" name="account">
	<br>
	Message: <input type="text" name="message">
	<br>
	<input type="submit" formmethod="get" formaction="/postmsg" value="post my message (via get)"><!-- # formmethod="post" -->
</form>
