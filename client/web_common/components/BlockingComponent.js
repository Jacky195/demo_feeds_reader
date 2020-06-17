import React from 'react';
import BlockUi from 'react-block-ui';
import LoadingIndicator from './LoadingIndicator';

export default class BlockingComponent extends React.Component {

    render() {
        const { isProcessing } = this.props;
        return (
            <BlockUi tag="div" blocking={isProcessing} loader={<LoadingIndicator />} className="height100Percentage">
                {this.props.children}
            </BlockUi>
        );
    }
}