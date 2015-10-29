var path = require('path'),
    ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    devtool: "source-map",
    entry: {
        app: ['./app/main.jsx']
    },
    output: {
        path: path.resolve(__dirname, '../static'),
        publicPath: '/',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            // Babel loader
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel?optional[]=runtime'
            },
            // CSS loader
            // {
            //     test: /\.css$/,
            //     loader: ExtractTextPlugin.extract('style-loader', 'css-loader?-minimize')
            // },
            //SASS/SCSS
            {
                test: /\.(sass|scss)$/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader?-minimize!sass-loader')
            }
        ]
    },
    resolve: {
        // where to find modules
        modulesDirectories: [
            'node_modules',
            'resources',
            'static',
            'app'
        ],
        extensions: ['.js', '.json', '.jsx', '']
    },
    plugins: [
        new ExtractTextPlugin('styles.css')
    ]
}