import React from 'react';
import { Input } from 'reactstrap';
import { MiscUtils } from '../../../web_common/extras';

export default class DropdownSelection extends React.Component{
    render() {
        const { optionList, onChangeCallback, currentValue } = this.props;
        return (
            <Input type="select" name="select" value={currentValue} onChange={(e) => onChangeCallback(e.target.value)}>
                {
                    optionList.map((option) =>
                        <option value={option.value} key={MiscUtils.generateId()}>
                            { option.text }
                        </option>
                    )
                }
            </Input>
        );
    }
}