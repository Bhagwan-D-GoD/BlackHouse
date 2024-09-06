# Dashboard Application

## Overview

This application features a dynamic dashboard built with Next.js and integrates with a Django backend. It displays various types of charts, including Candlestick, Line, Bar, and Pie charts, with data fetched from the backend. Users can filter the charts based on time periods.

## Libraries and Tools Used

### Frontend
- **Next.js (14.2.8)**: React-based framework for server-side rendering and static site generation.
- **react-chartjs-2**: Wrapper for Chart.js to create charts in React.
- **chart.js**: Charting library used to render charts.
- **Bootstrap**: CSS framework for responsive design and styling.
- **Lightweight Charts**: Library for rendering Candlestick charts.

### Backend
- **Django**: Python web framework used for building the API and managing data.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite/PostgreSQL**: Database options for storing application data.

## Setup and Running the Application

### Clone the Repository

```bash
git clone https://github.com/Bhagwan-D-GoD/BlackHouse.git
cd blackhouse

### Frontend Setup

1. **Navigate to the Frontend Directory**

    ```bash
    cd blackhouse/frontend
    ```

2. **Install Dependencies**

    Ensure you have Node.js and npm installed. Then, run:

    ```bash
    npm install
    ```

3. **Run the Development Server**

    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:3000`.

### Backend Setup

1. **Navigate to the Backend Directory**

    ```bash
    cd blackhouse/backend
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    The backend will be available at `http://localhost:8000`.

## Approach and Thought Process

1. **Frontend Implementation**:
   - **Dynamic Charts**: Used `react-chartjs-2` and `chart.js` for Line, Bar, and Pie charts. Implemented responsive design with Bootstrap to ensure the dashboard looks good on various screen sizes.
   - **Candlestick Chart**: Used `Lightweight Charts` to render Candlestick charts due to its performance and flexibility. Implemented data validation to handle cases where data is empty or null.

2. **Backend Implementation**:
   - **API Development**: Built Django APIs to serve chart data. Ensured data is fetched dynamically based on user input and provided endpoints for different types of charts.
   - **Data Handling**: Implemented logic to handle various data formats and validate data before sending it to the frontend.

3. **Integration**:
   - **Frontend-Backend Communication**: Integrated the frontend with the Django backend using API calls to fetch and display data in charts. Implemented filter options to allow users to select the time period for data visualization.

4. **Error Handling**:
   - Added error handling on the frontend to display messages when data is not received properly. Ensured a smooth user experience even when data is missing or incorrect.

## Future Enhancements

- **Enhanced Filtering**: Improve filtering options for more granular data selection.
- **Additional Chart Types**: Add more chart types and customization options.
- **Performance Optimization**: Optimize chart rendering for large datasets.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Next.js](https://nextjs.org/)
- [Chart.js](https://www.chartjs.org/)
- [React](https://reactjs.org/)
- [Django](https://www.djangoproject.com/)
- [Lightweight Charts](https://tradingview.github.io/lightweight-charts/)
