import {React, useState} from 'react'
import photo from '../img/headerphoto.png'
import top10 from '../img/Component 1.png'
import top5 from '../img/Component 2.png'
import DatePicker from "react-datepicker";
import PostCard from '../components/PostCard';
import Top5Tab from '../components/Top5Tab';
import { MDBDropdown, MDBDropdownItem, MDBDropdownToggle, MDBDropdownMenu } from 'mdb-react-ui-kit';
import HotTopicCard from '../components/HotTopicCard';

// Hot topics
const HotTopics = () => {
  const [date, setDate] = useState(new Date());
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();

  const [selectedOption, setSelectedOption] = useState('10');
  const handleOptionSelect = (option) => {
    setSelectedOption(option);
    // setSortOrder(option === 'Price Ascending' ? 'asc' : 'desc');
  };
  return (
    <>
      <div className='image_wrapper'>
        <img className='img-header' src={photo} alt='header photo'/>
        <div class="overlay overlay_2">
        <h1>What's new today?</h1> 
      </div>
      
      </div>
      <div className='date-picker d-flex'>
        <h7>From </h7>
        <DatePicker
          selectsStart
          selected={startDate}
          onChange={date => setStartDate(date)}
          startDate={startDate}
          className='input-date'
        />
        <h7> to </h7>
        <DatePicker
          selectsEnd
          selected={endDate}
          onChange={date => setEndDate(date)}
          endDate={endDate}
          startDate={startDate}
          minDate={startDate}
          className='input-date'
      />
        <h7>Top</h7>
        <select class="form-select input-date" aria-label="Default select example">
          <option selected value="10">10</option>
          <option value="15">15</option>
          <option value="20">20</option>
        </select>
      </div>
      <div className='hot-topic-area'>
        <HotTopicCard />
      </div>
    </>
  )
}

export default HotTopics