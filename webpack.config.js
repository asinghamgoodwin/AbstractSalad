module.exports = {
    entry: './js/main.jsx',
    output: {
        filename: 'abstract-salad.js',
        publicPath: 'http://localhost:8080/assets'
    },
    module: {
        loaders: [{
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loader: 'babel'
        }]
    }
};
