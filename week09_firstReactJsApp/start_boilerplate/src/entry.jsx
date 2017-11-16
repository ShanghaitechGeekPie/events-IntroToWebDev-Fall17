import React from 'react';
import ReactDOM from 'react-dom';
import { MsgBox } from './msgbox.jsx';

class DoYouReallyKnowMeWrapper extends React.Component {
    render() {
        return <MsgBox />
    }
}

ReactDOM.render(
    <DoYouReallyKnowMeWrapper />,
    document.getElementById('app-main')
)
