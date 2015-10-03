var HelloWorld = React.createClass({
	render: function() {
		return <div>Hello, world!</div>;
	}
})

React.render(new HelloWorld(), document.getElementById('example'));