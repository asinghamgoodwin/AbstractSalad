var React = require('react');
var ReactDOM = require('react-dom');
var createFragment = require('react-addons-create-fragment');

var CATEGORIES = ['Greens','Protein','Other','Veggies'];
var COMMITMENTS =
	[
		{'category': 'Greens', 'name': 'Ilona', 'ingredients': 'food'},
		{'category': 'Other', 'name': 'Linz', 'ingredients': 'not food'},
	];

var Header = React.createClass({
	render: function() {
		return (
			<h1 className="siteTitle">Abstract Salad Factory!</h1>
		);
	}
});

var Commitment = React.createClass({
	render: function(){
		return (
			<span>
			<li>{this.props.commitment.ingredients} - {this.props.commitment.name}</li>
			</span>
		);
	}
});

var Form = React.createClass({
	render: function(){
		return (
			<form action={this.props.category} /*onSubmit={this.handleSubmit}*/>
	      		<label for='name'>Name</label>
	      		<input name="name" /*value={this.state.value}*/ /*onChange={this.handleChange.bind(null, 'name')}*/ style={{margin:'5px'}}/>
	     		<label for='ingredient'>Ingredient</label>
	     		<input name="ingredient" /*value={this.state.value} onChange={this.handleChange.bind(null, 'ingredient')}*/ style={{margin:'5px'}}/>
	     		<button type="submit" onSubmit="" style={{margin:'5px'}}>Submit</button>
     		</form>
		);
	},


	handleChange: function(field, e) {
    	this.setState({[field]: e.target.value});
  	},
  	handleSubmit: function(e) {
		e.preventDefault();
		var newState = this.state.ingredients;
		var newThing = {
		  name: this.state.name,
		  category: this.state.category,
		  ingredient: this.state.ingredient
		};
		newState.push(newThing);
		this.setState({ingredients: newState});
		//server.addIngredient(newThing);
	},
	getInitialState: function(){
    	return {ingredients: [], name: '', ingredient: ''};
	}
});

var CategoryBox = React.createClass({
	render: function(){
		var commitmentList = [];
		var self = this;
		this.props.commitments.forEach(function(commitment){
		 	if (self.props.category === commitment.category)
		 		commitmentList.push(<Commitment key={commitment} commitment={commitment} category={category} />)
		});
		//var formKey = "form" + {this.props.category}
		return (
			<div className="categoryBox">
				<h2 className="categoryTitle">{this.props.category}</h2>
				<ul>
					{commitmentList}
				</ul>
				<Form key={this.props.category} />
			</div>
		);
	}
})


var SaladContainer = React.createClass({
	render: function(){
		var categoryList = [];
		var self = this;
		this.props.categoryNames.forEach(function(category){
			categoryList.push(<CategoryBox category={category} commitments={self.props.commitments} key={category} />);
		});
		return (
			<div className="saladContainer">{categoryList}</div>
		);
	}
});

var App = React.createClass({
	render: function() {
		return (
			<div>
			<Header />
			<SaladContainer categoryNames={CATEGORIES} commitments={COMMITMENTS} />
			</div>
		);
	}
});

window.addEventListener('load', function() {
  ReactDOM.render(<App/>, document.getElementById('container'));
});


/*
var App = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Abstract Salad Factory!</h1>
        <SaladContainer />
        <Footer/>
      </div>
    );
  }
});

function prepdata(ingredients) {
  var data = {};

  ingredients.forEach(function(i) {
    if (data[i.category] === undefined)
      data[i.category] = [];
    data[i.category].push(i);
  });

  return data;
}

var Ingredients = React.createClass({

  render: function(){
    var ingredients = prepdata(this.state.ingredients);
    console.log(this.state);

    return(
      <div>
      
      <form onSubmit={this.handleSubmit}>
      <label for='name'>Name</label>
      <input name="name" value={this.state.value} onChange={this.handleChange.bind(null, 'name')} style={{margin:'5px'}}/>
      <select name="category" value={this.state.value} onChange={this.handleChange.bind(null, 'category')} style={{margin:'5px'}}>
      
      {this.state.categories.map(function(category) {
       return <option value={category.id}> {category.name} </option>;
      })}
      </select>
      <label for='ingredient'>Ingredient</label>
      <input name="ingredient" value={this.state.value} onChange={this.handleChange.bind(null, 'ingredient')} style={{margin:'5px'}}/>
      <button type="submit" onSubmit="" style={{margin:'5px'}}>Submit</button>
      </form>
      {Object.keys(ingredients).map(function(category) {
        return <div style={{display:'inline-block', verticalAlign: 'top', margin:'5px', border:'solid 1px black', padding: '10px'}}>
        <h3 style={{borderBottom: 'dotted 1px black'}}> {category}</h3>
        {ingredients[category].map(function(property){
          return <p>
          {property.name} - {property.ingredient}
          </p>;
        })}

        </div>;
      })}
      </div>
      );
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var newState = this.state.ingredients;
    var newThing = {
      name: this.state.name,
      category: this.state.category,
      ingredient: this.state.ingredient
    };
    newState.push(newThing);
    this.setState({ingredients: newState});
    server.addIngredient(newThing);

  },
  componentDidMount: function(){
    var self = this;
    server.getCategories().then(function(categories){
      self.setState(
        {categories}
      );
    });
    server.getIngredients().then(function(ingredients){
      self.setState(
        {'ingredients': ingredients}
      );
    });

  },

  handleChange: function(field, e) {
    this.setState({[field]: e.target.value});
  },
  getInitialState: function(){
    return {ingredients: [], name: '', categories: [], category: 'Greens', ingredient: ''};
  }
});

var Footer = React.createClass({
  render: function() {
    return (
      <div className="footer">
        "This app was created dojo-style by Jamal Carvalho (S2'15), Madelyn Ruth Freed (S2'15), Shad William Hopson (F1'15), Kristin Linn (F1'15), Elizabeth Sander (S2'15), Alicia Thilani Singham Goodwin (F1'15), Alex Takata (F1'15), Liene Verzemnieks (S2'15), and Weston Elliott Vial (S2'15)"
      </div>
    );  
  }
});

*/