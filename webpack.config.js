module.exports = {
    entry: './js/main.jsx',
    devtool: 'eval-source-map',
    output: {
        filename: 'static/abstract-salad.js',
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
