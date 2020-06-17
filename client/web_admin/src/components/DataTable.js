import React from 'react';
import { Table, Row, Col, Button } from 'reactstrap';
import Pager from './Pager';
import { DropdownSelection } from "./index";
import { PAGE_SIZE_OPTIONS } from '../config';
import { MiscUtils } from '../../../web_common/extras';


export default class DataTable extends React.Component{

    render() {
        const { header, data, pageLimitChangeCallback, pageSize, page } = this.props;
        return (
            <>
                <Table hover responsive size="sm">
                    <thead>
                        <tr>
                            {
                                header.map((col) =>
                                    <th key={MiscUtils.generateId()}>
                                        {col.text}
                                    </th>
                                )
                            }
                        </tr>
                    </thead>

                    <tbody>
                        {
                            data.map((row) =>
                                <tr key={MiscUtils.generateId()}>
                                    {
                                        header.map((col) =>
                                            <td key={MiscUtils.generateId()}>
                                                {row[col.value]}
                                            </td>
                                        )
                                    }
                                </tr>
                            )
                        }

                      </tbody>
                    </Table>

                    <Row>
                        <Col sm="1" xs="6">
                            <DropdownSelection optionList={PAGE_SIZE_OPTIONS}
                                               onChangeCallback={pageLimitChangeCallback}
                                               currentValue={pageSize}
                            />
                        </Col>
                        <Col sm={{ size: 4, offset: 7 }} xs="6" className="paddingTop10">
                            {
                                this.props.totalPage > 0 &&
                                <Pager {...this.props} />
                            }

                        </Col>
                    </Row>
            </>
        );
    }

}