const path = require('path');

const dotenv = require('dotenv');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CircularDependencyPlugin = require('circular-dependency-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');

const DIST = path.join(__dirname, 'build');

module.exports = function (env, argv) {
    const { mode } = argv;
    const port = 5000;
    const isProdBuild = mode === 'production';
    const isLocalBuild = mode === 'development';

    return {
        devServer: {
            contentBase: DIST,
            port: port,
            historyApiFallback: true,
            lazy: false,
            open: true,
        },

        devtool: isProdBuild ? 'source-map' : 'eval-cheap-source-map',

        entry: {
            app: './src/index.js',
        },

        optimization: {
            splitChunks: {
                cacheGroups: {
                    commons: {
                        test: /[\\/]node_modules[\\/]/,
                        name: 'shared',
                        chunks: 'all',
                    },
                },
            },
        },

        output: isProdBuild
            ? {
                assetModuleFilename: 'images/[name][ext]',
                chunkFilename: '[name].[contenthash:8].chunk.js',
                filename: '[name].[contenthash:8].chunk.js',
                publicPath: '/',
                path: DIST,
            }
            : {
                assetModuleFilename: 'images/[name][ext]',
                filename: '[name].bundle.js',
                publicPath: isLocalBuild ? 'http://localhost:' + port + '/' : '/',
                path: DIST,
            },

        performance: {
            hints: isProdBuild ? 'warning' : false,
            maxAssetSize: 300000,
        },

        plugins: [
            new MiniCssExtractPlugin(),

            isProdBuild
                ? new CircularDependencyPlugin({
                    exclude: /a\.js|node_modules/,
                    include: /src/,
                    // add errors to webpack instead of warnings
                    failOnError: true,
                    allowAsyncCycles: false,
                    cwd: process.cwd(),
                })
                : false,


            new CleanWebpackPlugin({ cleanStaleWebpackAssets: false }),

            new webpack.DefinePlugin({
                DEBUG: JSON.stringify(JSON.parse(isProdBuild ? 'false' : 'true')),
                'process.env': JSON.stringify(dotenv.config().parsed),
            }),

            new HtmlWebpackPlugin({
                template: path.join(__dirname, 'public', 'index.html'),
                minify: {
                    collapseWhitespace: false,
                    removeComments: true,
                },
                inject: 'body',
            }),
        ].filter(Boolean),

        resolve: {
            fallback: { crypto: false },
        },

        target: isProdBuild ? 'browserslist' : 'web',

        module: {
            rules: [
                {
                    test: /\.js$/,
                    include: [path.resolve(__dirname, 'src')],
                    exclude: /node_modules/,
                    use: 'babel-loader?cacheDirectory',
                },
                {
                    test: /\.css$/,
                    use: [
                        isProdBuild
                            ? {
                                loader: MiniCssExtractPlugin.loader,
                                options: {
                                    publicPath: '',
                                },
                            }
                            : 'style-loader',
                        {
                            loader: 'css-loader',
                            options: {
                                sourceMap: true,
                                modules: {
                                    localIdentName: '[folder]_[local]_[contentHash:8]',
                                },
                            },
                        },
                    ],
                },
                {
                    test: /\.(png|jpe?g|gif|svg)$/i,
                    type: 'asset/resource',
                },
            ],
        },
    };
};
