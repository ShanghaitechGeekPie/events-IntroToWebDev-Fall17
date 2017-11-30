// Path library that dynamically generates path string
const path = require('path');

// HtmlWebPackPlugin for auto-generation of HTML file
const htmlWebPackPlugin = require('html-webpack-plugin');

// Of course, we need Webpack
const webpack = require('webpack');

// all the settings in module.exports
module.exports = {
    entry: './src/entry.jsx',
    output: {
        filename: '[name].dist.js',
        path: path.resolve(__dirname, 'dist')
    },
    plugins: [
        new htmlWebPackPlugin({
            title: 'React-Router and Fetch DEMO',
            inject: 'body',
            template: path.join(__dirname, 'src', 'html', 'base.ejs'),
            appMountId: 'app-main'
        })
    ],
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    }
}