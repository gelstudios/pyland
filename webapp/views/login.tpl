<title>tinybbs</title>
<div class=topbar>
<h1>tinybbs login</h1>
</div>
<br>
<form action="/login" method="post"> <!--# method="post"-->
	username: <input type="text" name="username">
	<br>
	password: <input type="text" name="password">
	<br>
	<input type="submit" formmethod="post" formaction="/login" value="login"><!-- # formmethod="post" -->
	<a href="/reset">forgot?</a>
</form>
