import { getAllTools, getCategories } from '@/lib/yaml';
import ExploreClient from '@/components/ExploreClient';

export const metadata = {
  title: 'Explore AI Tools - AI Landscape',
  description: 'The most comprehensive AI developer ecosystem tool library, including foundation models, dev frameworks, vector databases, etc.',
};

export default function ExplorePageEn() {
  const tools = getAllTools();
  const categories = getCategories();

  return <ExploreClient initialTools={tools} categories={categories} locale="en" />;
}
