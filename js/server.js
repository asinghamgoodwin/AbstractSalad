module.exports = {
    getIngredients: function() {
        return fetch('/salad').then(function(resp) {
            return resp.json().then(function (data) {
                return data.Ingredients;
            });
        });
    },

    addIngredient: function(data) {
        var form = new FormData();
        Object.keys(data).forEach(function(key) {
            form.append(key, data[key]);
        });
        return fetch('/add', {
            method: 'POST',
            body: form
        });
    }
};
