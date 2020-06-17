const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const dotenv = require('dotenv');


const COMPONENT = {
    USER: 'user',
    ADMIN: 'admin'
};

module.exports = (env) => {
    // mode: development / staging / production
    // component: user / admin

    const { mode, component } = env;
    dotenv.config({ path: `./.env.${mode}`});

    const {
        PORT_CLIENT_USER,
        PORT_CLIENT_ADMIN
    } = process.env;

    let PORT = null;
    if (component === COMPONENT.USER)
        PORT = PORT_CLIENT_USER;
    else if (component === COMPONENT.ADMIN)
        PORT = PORT_CLIENT_ADMIN;

    return {
        entry: path.join(__dirname, `./web_${component}/src/index.js`),
        output: {
            path: path.resolve(__dirname, `./web_${component}/dist`),
            publicPath: '/',
            filename: '[name].[hash].js'
        },

        module: {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    exclude: [/node_modules/],
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env','@babel/react',{'plugins': ['@babel/plugin-proposal-class-properties']}]
                        }
                    }
                },
                {
                    test: /\.(scss|css)$/,
                    use: [
                        {
                            loader: "style-loader" // creates style nodes from JS strings
                        },
                        {
                            loader: "css-loader" // translates CSS into CommonJS
                        },
                        {
                            loader: "resolve-url-loader"
                        },
                        {
                            loader: "sass-loader" // compiles Sass to CSS
                        }
                    ]
                },
                {
                    test: [/\.bmp$/, /\.gif$/, /\.jpg$/, /\.jpe?g$/, /\.png$/],
                    loader: 'url-loader',
                    options: {
                        // limit: 10000,
                        name: '[path][name].[hash].[ext]',
                    },
                },
                {
                    test: /\.svg$/,
                    loader: 'svg-inline-loader'
                },
                {
                    test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: '[name].[ext]',
                                outputPath: 'fonts/'
                            }
                        }
                    ]
                }
            ]
        },


        optimization: {
            splitChunks: {
                cacheGroups: {
                    vendor: {
                        chunks: "initial",
                        test: path.resolve(process.cwd(), "node_modules"),
                        name: "vendor",
                        enforce: true
                    }
                }
            }
        },

        devServer: {
            contentBase: `./web_${component}/public`,
            host: '0.0.0.0',
            port: PORT,
            inline: true,
            historyApiFallback: true, // de su dung B

            // for docker
            watchOptions: {
                aggregateTimeout: 500, // delay before reloading
                poll: 1000 // enable polling since fs events are not supported in docker
            }
        },

        // Development Tools (Map Errors To Source File)
        devtool: 'source-map',

        plugins: [
            new webpack.HotModuleReplacementPlugin(),
            new HtmlWebpackPlugin({
                template: `web_${component}/public/index.html`,
                filename: 'index.html',
                hash: true
            })
        ]
    };
};