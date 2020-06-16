import React from 'react';
import { Input } from 'reactstrap';
import { MiscUtils } from '../../../web_common/extras';

export default class DropdownSelection extends React.Component{
    render() {
        const { optionList } = this.props;
        return (
            <Input type="select" name="select">
                {
                    optionList.map((option, idx) =>
                        <option value={option.value} key={MiscUtils.generateId()}>{ option.text }</option>
                    )
                }
            </Input>
        );
    }

}