import React from 'react';
import { Loader } from 'react-loaders';

export default class LoadingIndicator extends React.Component {
    render (){
        return <Loader active type="line-scale" color="#02a17c"/>;
    }
}

