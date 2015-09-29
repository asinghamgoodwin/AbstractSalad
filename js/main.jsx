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
        <Footer/>
      </div>
    );
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
