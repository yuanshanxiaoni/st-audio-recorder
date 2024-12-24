import { library } from "@fortawesome/fontawesome-svg-core"
import { fas } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import React from "react"
import {
  Streamlit,
  ComponentProps,
  withStreamlitConnection,
} from "streamlit-component-lib"
import axios from "axios";

library.add(fas)

interface AudioRecorderState {
  recording: boolean
  color: string
}

interface PythonArgs {
  status: string
}

class AudioRecorderUI extends React.Component<ComponentProps, AudioRecorderState> {
  private pollingInterval: number | null = null;

  constructor(props: ComponentProps) {
    super(props)
    this.state = {
      recording: false,
      color: this.props.args["neutral_color"]
    }
  }

  componentDidMount() {
    Streamlit.setFrameHeight()
    this.updateStatus(this.props.args.status || "init")

    const msec = parseInt(this.props.args["polling_interval"]) || 600;
    this.pollingInterval = window.setInterval(this.pollRecordingStatus, msec);
  }

  componentDidUpdate(prevProps: ComponentProps) {
    if (prevProps.args.status !== this.props.args.status) {
      this.updateStatus(this.props.args.status)
    }
  }

  pollRecordingStatus = async () => {
    try {
      const get_status_url = this.props.args["get_status_url"];
      console.log("Polling recording props:", this.props);
      console.log("Polling recording status from:", get_status_url);
      const response = await axios.get(get_status_url);
      const { is_recording } = response.data;

      if (is_recording !== this.state.recording ) {
        this.updateStatus(is_recording ? "start" : "stop");
        this.setState({
          recording: is_recording,
          color: is_recording ? this.props.args["recording_color"] : this.props.args["neutral_color"],
        });
      }
    } catch (error) {
      console.error("Error fetching recording status:", error);
    }
  };


  updateStatus(status: string) {
    if (status === "stop" && this.state.recording) {
      this.setState({
        recording: false,
        color: this.props.args["neutral_color"]
      }, () => {
        Streamlit.setComponentValue({ status: "stop" })
      })
    } else {
      Streamlit.setComponentValue({ status: status })
    }
  }

  onClicked = () => {
    if (this.state.recording) {
      this.setState({
        recording: false,
        color: this.props.args["neutral_color"]
      }, () => {
        Streamlit.setComponentValue({ status: "stop" })
      })
    } else {
      this.setState({
        recording: true,
        color: this.props.args["recording_color"]
      }, () => {
        Streamlit.setComponentValue({ status: "start" })
      })
    }
  }

  render() {
    return (
      <span>
        <button
          aria-hidden="false"
          aria-label="Record"
          onClick={this.onClicked}
          style={{
            backgroundColor: "transparent",
            border: "none",
            cursor: "pointer",
          }}
        >
          <FontAwesomeIcon
            // @ts-ignore
            icon={this.props.args["icon_name"]}
            style={{ color: this.state.color }}
            size={this.props.args["icon_size"]}
          />
        </button>
      </span>
    )
  }
}

export default withStreamlitConnection(AudioRecorderUI)
