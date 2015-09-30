var React = require('react');
var server = require('./server');


// The server module provides two functions for retrieving
// and saving data to the server. They both return promises.

// getIngredients returns an array of the current ingredients
// added to a salad:
//
// server.getIngredients().then(function(ingredients) {
//   console.log(ingredients);
// });

// addIngredient saves a new ingredient to the server:
//
// server.addIngredient({
//   name: 'Allie',
//   category: 'Greens',
//   ingredient: 'Arugula'
// });

var App = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Abstract Salad Factory!</h1>
        <Ingredients/>
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
      {Object.keys(ingredients).map(function(category) {
       return <option value={category}> {category} </option>;
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
    return {ingredients: [], name: '', category: 'Greens', ingredient: ''};
  }
});

var Footer = React.createClass({
  render: function() {
    return (
      <div className="footer">
        This app was created dojo-style by Jamal Carvalho (S2'15), Madelyn Ruth Freed (S2'15), Shad William Hopson (F1'15), Kristin Linn (F1'15), Elizabeth Sander (S2'15), Alicia Thilani Singham Goodwin (F1'15), Alex Takata (F1'15), Liene Verzemnieks (S2'15), and Weston Elliott Vial (S2'15)
      </div>
    );  
  }
});

window.addEventListener('load', function() {
  React.render(<App/>, document.getElementById('app'));
});
